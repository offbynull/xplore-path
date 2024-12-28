import argparse
import sys
from pathlib import Path
from typing import Any

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import ThreadedCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

import xplore_path.path.path
from xplore_path.repl.utils import print_line
from xplore_path.evaluator import evaluate
from xplore_path.paths.filesystem_path import FileSystemPath
from xplore_path.raise_parse_error_listener import ParseException
from xplore_path.repl.path_completer import PathCompleter, TOKENS


def _single_result_to_line(v: Any, full_labels: bool) -> list[tuple[str, str]]:
    ret = []
    if isinstance(v, xplore_path.path.path.Path):
        if not full_labels:
            ret += [('fg:ansiwhite bold', f'{v.label()}')]
        else:
            for l in v.full_label()[1:]:
                if l in TOKENS:
                    l = l.replace('\'', '\'\'')
                    l = f'\'{l}\''
                ret.append(('fg:ansigray', '/'))
                ret.append(('fg:ansiwhite bold', f'{l}'))

        highlight = ''
        cnt = len(v.all_children())
        if cnt > 0:
            highlight = 'fg:ansiwhite bold'
        ret += [
            ('', ' child_count='),
            (highlight, f'{cnt}')
        ]
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


def main(active_dir_path: Path):
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
            if isinstance(query_res, list):
                toolbar_text = f'{len(query_res)} result' + ('s' if query_res else '')
            else:
                toolbar_text = f'1 result'
        toolbar_text += '  ' + ('[FULL LABELS]' if full_labels else '[LOCAL LABELS]')
        toolbar_text += ' ' + ('[TRUNC]' if truncate_long_lines else '[NO TRUNC]')
        return toolbar_text


    p = FileSystemPath.create_root_path(active_dir_path)
    completer = ThreadedCompleter(PathCompleter(p))  # Wrap in ThreadedCompleter because completions can take a while
    session = PromptSession(
        completer=completer,
        complete_while_typing=True,
        style=_STYLES,
        history=FileHistory(Path('~/.xplore_path_history').expanduser()),
        key_bindings=bindings
    )

    session.app.print_text([
        ('           ', _ASCII_LOGO + '\n'),
        ('           ', '\n'),
        ('           ', 'Xplore Path REPL\n'),
        ('           ', '----------------\n'),
        ('           ', f'Active directory: {active_dir_path}\n'),
        ('           ', '\n'),
        ('           ', 'Keys:\n'),
        ('fg:ansiblue', '  Enter'), ('', ' to execute\n'),
        ('fg:ansiblue', '  Tab'), ('', ' for autocomplete\n'),
        ('fg:ansiblue', '  ↑↓'), ('', ' to navigate history\n'),
        ('fg:ansiblue', '  Ctrl-L'), ('', ' to turn on/off full labels in outputs\n'),
        ('fg:ansiblue', '  Ctrl-T'), ('', ' to turn on/off truncating outputs\n'),
        ('fg:ansiblue', '  Ctrl-C'), ('', ' to exit\n'),
        ('           ', '\n'),
        ('           ', 'Examples:\n'),
        ('fg:ansiblue', '  /*'), ('', ' - get all children\n'),
        ('fg:ansiblue', '  //*'), ('', ' - get all descendants (may take a long time)\n'),
        ('fg:ansiblue', '  /apple/*[./cherry]'), ('', ' - get all children of apple who have a child named cherry\n'),
        ('           ', '\n')
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
            query_res = evaluate(p, expr)
            if not isinstance(query_res, list):
                query_res = [query_res]
            for v in query_res:
                print_line(session, _single_result_to_line(v, full_labels), truncate_long_lines)
        except ParseException as e:
            query_res = None
            print(f'Unable to parse expression: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Xplore Path REPL')
    parser.add_argument(
        '--path',
        type=str,
        default=str(Path.cwd().absolute()),
        help='path to top-level directory to explore (default: current directory)'
    )
    args = parser.parse_args()
    path = Path(args.path)
    if not path.exists():
        print(f'Path does not exist: {path}')
        sys.exit(1)
    if not path.is_dir():
        print(f'Path is not directory: {path}')
        sys.exit(1)
    main(path)
