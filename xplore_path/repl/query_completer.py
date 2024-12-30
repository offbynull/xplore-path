from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document

import xplore_path.path.path
from xplore_path.evaluator import Evaluator
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath
from xplore_path.repl.utils import TOKENS, fix_label_for_expression


class QueryCompleter(Completer):
    def __init__(self, evaluator: Evaluator, p: FileSystemPath):
        self.evaluator = evaluator
        self.p = p

    def get_completions(self, document: Document, complete_event):
        if document.text == '':
            yield Completion('/', start_position=0)
            yield Completion('/*', start_position=0)
            yield Completion('//*', start_position=0)
        else:
            text_before = document.text[:document.cursor_position+1]
            last_slash_1_idx = text_before.rfind('/')
            last_slash_2_idx = text_before.rfind('//')
            last_var_idx = text_before.rfind('$')
            last_wrap_start_idx = max(text_before.rfind('['), text_before.rfind('('))
            last_wrap_stop_idx = max(text_before.rfind(']'), text_before.rfind(')'))
            type_, idx_ = max(
                [
                    ('slash_1', last_slash_1_idx),
                    ('slash_2', last_slash_2_idx),
                    ('var', last_var_idx),
                    ('wrap_start', last_wrap_start_idx),
                    ('wrap_stop', last_wrap_stop_idx)
                ],
                key=lambda x: x[1]
            )
            if idx_ != -1:
                partial_query = text_before[:idx_ + 1]
                inject_offset = idx_ - document.cursor_position
                if type_ in {'slash_1', 'slash_2'}:
                    partial_query = partial_query.removesuffix('//')
                    partial_query = partial_query.removesuffix('/')
                    if partial_query == '':
                        partial_query = '/'
                    unfinished_token = text_before[idx_ + 1:]
                    yield from self._exec_for_completions(partial_query, inject_offset, unfinished_token)
                elif type_ == 'var':
                    for var in self.evaluator.variables:
                        yield Completion(fix_label_for_expression(var), start_position=inject_offset)
                elif type_ == 'wrap_start':
                    ...  # Skip this case?
                elif type_ == 'wrap_stop':
                    partial_query = partial_query.removesuffix(']')
                    partial_query = partial_query.removesuffix(')')
                    if partial_query == '':
                        partial_query = '/'
                    unfinished_token = text_before[idx_ + 1:]
                    yield from self._exec_for_completions(partial_query, inject_offset, unfinished_token)
        for var in self.evaluator.variables:
            # add style to debug: style='bg:ansigray fg:ansiblack'
            yield Completion(fix_label_for_expression(var), start_position=0)
        for token in TOKENS:
            # add style to debug: style='bg:ansigray fg:ansiblack'
            yield Completion(token, start_position=0)

    def _exec_for_completions(self, partial_query: str, inject_offset: int, unfinished_token: str):
        try:
            res = self.evaluator.evaluate(self.p, partial_query)
            yield Completion('/*', start_position=inject_offset)
            yield Completion('//*', start_position=inject_offset)
            for p in res:
                for child_p in p.all_children():
                    if isinstance(child_p, xplore_path.path.path.Path) and str(child_p.label()).startswith(unfinished_token):
                        # add style to debug: style='bg:ansiyellow fg:ansiblack'
                        label = fix_label_for_expression(child_p.label())
                        yield Completion(f'/{label}/*', start_position=inject_offset)
                        yield Completion(f'/{label}/', start_position=inject_offset)
                        yield Completion(f'/{label}', start_position=inject_offset)
            for p in res:
                for child_p in p.all_children():
                    if isinstance(child_p, xplore_path.path.path.Path):
                        label = fix_label_for_expression(child_p.label())
                        yield Completion(f'/{label}/*', start_position=inject_offset)
                        yield Completion(f'/{label}/', start_position=inject_offset)
                        yield Completion(f'/{label}', start_position=inject_offset)
        except Exception as e:
            # print(partial_query)
            # print(f'{e}')
            ...
