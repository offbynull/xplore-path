from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document

import xplore_path.path.path
from xplore_path.evaluator import evaluate
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath
from xplore_path.repl.utils import TOKENS, fix_label_for_expression


class PathCompleter(Completer):
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
                partial_query = partial_query.removesuffix('//')
                partial_query = partial_query.removesuffix('/')
                if partial_query == '':
                    partial_query = '/'
                unfinished_token = text_before[end_idx+1:]
                inject_offset = end_idx - document.cursor_position
                try:
                    res = evaluate(self.p, partial_query)
                    yield Completion('/*', start_position=inject_offset)
                    yield Completion('//*', start_position=inject_offset)
                    for p in res:
                        for child_p in p.all_children():
                            if isinstance(child_p, xplore_path.path.path.Path) and str(child_p.label()).startswith(unfinished_token):
                                # add style to debug: style='bg:ansiyellow fg:ansiblack'
                                label = fix_label_for_expression(child_p.label())
                                yield Completion(f'/{label}', start_position=inject_offset)
                    for p in res:
                        for child_p in p.all_children():
                            if isinstance(child_p, xplore_path.path.path.Path):
                                label = fix_label_for_expression(child_p.label())
                                yield Completion(f'/{label}', start_position=inject_offset)
                except Exception as e:
                    # print(partial_query)
                    # print(f'{e}')
                    ...
        for token in TOKENS:
            # add style to debug: style='bg:ansigray fg:ansiblack'
            yield Completion(token, start_position=0)
