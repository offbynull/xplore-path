import argparse
import re
import sys
from pathlib import Path

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion, ThreadedCompleter
from prompt_toolkit.document import Document
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

import xplore_path.path.path
from xplore_path.evaluator import evaluate
from xplore_path.paths.filesystem_path import FileSystemPath
from xplore_path.raise_parse_error_listener import ParseException

tokens_text = (Path(__file__).parent / 'XPath31GrammarLexer.tokens').read_text()
tokens = [re.search(r"'(.*?)'", line).group(1) for line in tokens_text.splitlines() if '\'' in line]
tokens = sorted(tokens, reverse=True)


class CustomCompleter(Completer):
    def __init__(self, p: FileSystemPath):
        self.p = p

    def get_completions(self, document: Document, complete_event):
        if document.text == '':
            yield Completion('/', start_position=0)
            yield Completion('/*', start_position=0)
            yield Completion('//*', start_position=0)
        else:
            text_before = document.text[:document.cursor_position+1]
            end_idx = max(text_before.rfind('//'), text_before.rfind('/'))
            if end_idx != -1:
                partial_query = text_before[:end_idx+1]
                unfinished_token = text_before[end_idx+1:]
                inject_offset = end_idx - document.cursor_position
                try:
                    res = evaluate(self.p, partial_query)
                    for p in res:
                        for child_p in p.all_children():
                            if isinstance(child_p, xplore_path.path.path.Path) and type(child_p.label()) == str and child_p.label().startswith(unfinished_token):
                                yield Completion(f'/{child_p.label()}', start_position=inject_offset, style='bg:ansiyellow fg:ansiblack')
                    yield Completion('/*', start_position=inject_offset)
                    yield Completion('//*', start_position=inject_offset)
                    for p in res:
                        for child_p in p.all_children():
                            if isinstance(child_p, xplore_path.path.path.Path):
                                yield Completion(f'/{child_p.label()}', start_position=inject_offset)
                except Exception:
                    ... # do nothing
        for token in tokens:
            yield Completion(token, start_position=0, style='bg:ansigray fg:ansiblack')



style = Style.from_dict({
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
    completer = ThreadedCompleter(CustomCompleter(p))  # Wrap in ThreadedCompleter because completions can take a while
    session = PromptSession(
        completer=completer,
        complete_while_typing=True,
        style=style,
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

    def print_output_line(line):
        nonlocal session
        if not truncate_long_lines:
            session.app.print_text(line + [('', '\n')])
            return
        max_width = session.app.output.get_size().columns
        next_line = []
        curr_width = 0
        for style, text in line:
            next_curr_width = curr_width + len(text)
            if next_curr_width >= max_width:
                text = text[:max_width-curr_width]  # truncate to match max_width
                text = text[:-1]  # remove last char as well
                next_line.append((style, text)) # add
                next_line.append(('bg:ansired', '>')) # replace last char with a red > to indicate spillover
            else:
                next_line.append((style, text))
            curr_width = next_curr_width
        next_line.append(('', '\n'))
        session.app.print_text(next_line)


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
            if isinstance(query_res, list):
                for v in query_res:
                    # trim root node's label when printing
                    if isinstance(v, xplore_path.path.path.Path):
                        label = v.full_label() if full_labels else v.label()
                        print_output_line([
                            ('', '  '), ('fg:ansiwhite bold', f'{label}'), ('fg:ansigray', f': {v.value()}')
                        ])
                    else:
                        print_output_line([
                            ('', '  '), ('fg:ansigray', f'{v}')
                        ])
            else:
                print_output_line([
                    ('', '  '), ('fg:ansigray', f'{query_res}')
                ])
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
