import argparse
import shutil
import sys
from pathlib import Path
from tempfile import gettempdir
from typing import Any

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import ThreadedCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

import xplore_path.path
from xplore_path.evaluator import Evaluator
from xplore_path.repl.query_completer import QueryCompleter
from xplore_path.repl.utils import print_line, fix_label_for_expression
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath, FileSystemPathContext, NoticeType
from xplore_path.raise_parse_error_listener import ParseException
from xplore_path.sequence import Sequence, SingleWrapSequence


def _single_result_to_line(v: Any, full_labels: bool) -> list[tuple[str, str]]:
    ret = []
    if isinstance(v, xplore_path.path.Path):
        if not full_labels:
            ret += [('fg:ansiwhite bold', f'{v.label()}')]
        else:
            for l in v.full_label()[1:]:
                l = fix_label_for_expression(l)
                ret.append(('fg:ansigray', '/'))
                ret.append(('fg:ansiwhite bold', f'{l}'))
        #
        # highlight = ''
        # cnt = len(v.all_children())
        # if cnt > 0:
        #     highlight = 'fg:ansiwhite bold'
        # ret += [
        #     ('', ' child_count='),
        #     (highlight, f'{cnt}')
        # ]
        data = v.value()
    else:
        ret += [('', '<NO_LABEL> ')]
        data = v

    ret += [('', ' value=')]
    if type(data) in {int, float, bool, str}:
        ret += [('fg:ansiwhite bold', f'({type(data).__name__}) {data}')]
    else:
        ret += [('', f'({type(data).__name__}) {data}')]

    return ret


_STYLES = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222'
})


# https://patorjk.com/software/taag/#p=display&f=Small&t=Xplore%20Path
_ASCII_LOGO = r'''
__  __     _               ___      _   _    
\ \/ /_ __| |___ _ _ ___  | _ \__ _| |_| |_  
 >  <| '_ \ / _ \ '_/ -_) |  _/ _` |  _| ' \ 
/_/\_\ .__/_\___/_| \___| |_| \__,_|\__|_||_|
     |_|                                     
'''.strip()


def _cache_notifier(notice_type: NoticeType, child_path: Path):
    if notice_type in {NoticeType.ARCHIVE_CACHE_START, NoticeType.DATA_CACHE_START}:
        print(f'Caching {child_path}... ', end='', flush=True)
    elif notice_type in {NoticeType.DATA_CACHE_COMPLETE, NoticeType.ARCHIVE_CACHE_COMPLETE}:
        print(f'ok', flush=True)
    elif notice_type in {NoticeType.DATA_CACHE_ERROR, NoticeType.ARCHIVE_CACHE_ERROR}:
        print(f'error', flush=True)


def prompt(evaluator: Evaluator, query_path: Path, cache_path: Path):
    bindings = KeyBindings()

    full_labels = True
    @bindings.add('c-l')
    def _(event):
        nonlocal full_labels
        full_labels = not full_labels

    truncate_long_lines = True
    @bindings.add('c-t')
    def _(event):
        nonlocal truncate_long_lines
        truncate_long_lines = not truncate_long_lines

    query_res = None
    def get_toolbar_text():
        nonlocal query_res
        nonlocal full_labels
        nonlocal truncate_long_lines
        if query_res is None:
            toolbar_text = 'Type query and hit enter'
        else:
            if isinstance(query_res, Sequence):
                toolbar_text = f'{sum(1 for _ in query_res)} result' + ('s' if query_res else '')
            else:
                toolbar_text = f'1 result'
        toolbar_text += '  ' + ('[FULL LABELS]' if full_labels else '[LOCAL LABELS]')
        toolbar_text += ' ' + ('[TRUNC]' if truncate_long_lines else '[NO TRUNC]')
        return toolbar_text


    p = FileSystemPath.create_root_path(
        query_path,
        FileSystemPathContext(
            workspace=cache_path,
            cache_notifier=_cache_notifier
        )
    )
    p_cached_only = FileSystemPath.create_root_path(
        query_path,
        FileSystemPathContext(
            workspace=cache_path,
            cache_only_access=True
        )
    )
    completer = ThreadedCompleter(
        QueryCompleter(
            evaluator,
            p_cached_only
        )
    )  # Wrap in ThreadedCompleter because can take a while
    session = PromptSession(
        completer=completer,
        complete_while_typing=True,
        style=_STYLES,
        history=FileHistory(Path('~/.xplore_path_history').expanduser()),
        key_bindings=bindings
    )

    session.app.print_text([
        ('            ', _ASCII_LOGO + '\n'),
        ('            ', '\n'),
        ('            ', 'Xplore Path REPL\n'),
        ('            ', '----------------\n'),
        ('            ', f'Active directory:\n'),
        ('fg:ansiwhite', f'  {query_path}\n'),
        ('            ', '\n'),
        ('            ', 'Keys:\n'),
        ('fg:ansiblue ', '  Enter'), ('', ' to execute\n'),
        ('fg:ansiblue ', '  Tab'), ('', ' for autocomplete suggestions\n'),
        ('fg:ansiblue ', '  ↑↓'), ('', ' to navigate history\n'),
        ('fg:ansiblue ', '  Ctrl-L'), ('', ' to turn on/off full labels in outputs\n'),
        ('fg:ansiblue ', '  Ctrl-T'), ('', ' to turn on/off truncating outputs\n'),
        ('fg:ansiblue ', '  Ctrl-C'), ('', ' to exit\n'),
        ('            ', '\n'),
        ('            ', 'Examples:\n'),
        ('fg:ansiblue ', '  /*'), ('', ' - get all children\n'),
        ('fg:ansiblue ', '  //*'), ('', ' - get all descendants (may take a long time)\n'),
        ('fg:ansiblue ', '  /apple/*[./cherry]'), ('', ' - get all children of apple who have a child named cherry\n'),
        ('            ', '\n'),
        ('fg:ansiyellow', 'WARNING: '), ('', 'Autocomplete suggestions are best-effort and may not always be '
                                             'correct and / or may not always be exhaustive.\n'),
        ('            ', '\n')
    ])

    default_prompt = ''
    while True:
        try:
            expr = session.prompt('> ', default=default_prompt, bottom_toolbar=get_toolbar_text)
            default_prompt = expr
        except (KeyboardInterrupt, EOFError):
            print('Exiting.')
            break
        try:
            query_res = evaluator.evaluate(p, expr)
            if not isinstance(query_res, Sequence):
                query_res = SingleWrapSequence(query_res)
            for v in query_res:
                print_line(session, _single_result_to_line(v, full_labels), truncate_long_lines)
        except ParseException as e:
            query_res = None
            print(f'Unable to parse expression: {e}')


def precache(evaluator: Evaluator, query_path: Path, cache_path: Path) -> None:
    p = FileSystemPath.create_root_path(
        query_path,
        FileSystemPathContext(
            workspace=cache_path,
            cache_notifier=_cache_notifier
        )
    )
    evaluator.evaluate(p, '//*')
    print('Pre-cache complete')


def main():
    parser = argparse.ArgumentParser(
        description='Xplore Path REPL',
        add_help=False
    )
    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help="Display help message and exit."
    )
    parser.add_argument(
        '--path',
        type=str,
        default=str(Path.cwd().absolute()),
        help='Path to directory to query (default: current directory).'
    )
    parser.add_argument(
        '--cache-path',
        type=str,
        default=str(Path(f'{gettempdir()}/xplore_path_cache')),
        help='Path to directory to use for caching (default: temporary directory).'
    )
    parser.add_argument(
        '--cache-preload',
        action='store_true',
        help='Preload cache at launch (may take some time at launch but quicker feedback).'
    )
    parser.add_argument(
        '--cache-clear',
        action='store_true',
        help='Clear cache at launch.'
    )
    args = parser.parse_args()
    query_path = Path(args.path)
    if not query_path.exists():
        print(f'Path does not exist: {query_path}')
        sys.exit(1)
    if not query_path.is_dir():
        print(f'Path is not directory: {query_path}')
        sys.exit(1)
    cache_path = Path(args.cache_path)
    evaluator = Evaluator()
    if args.cache_clear:
        print(f'Clearing cache at {cache_path}...')
        shutil.rmtree(cache_path, ignore_errors=True)
    if args.cache_preload:
        print(f'Preloading cache to {cache_path} (may take a while)...')
        precache(evaluator, query_path, cache_path)
    prompt(evaluator, query_path, cache_path)


if __name__ == '__main__':
    main()