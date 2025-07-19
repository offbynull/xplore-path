from __future__ import annotations

import ast
import tokenize
from typing import Any

from xplore_path.nodes.simple.simple_node import SimpleNode
from xplore_path.null import Null
from xplore_path.node import Node, ParentBlock


class PythonAstNode(Node):
    """
    ``Node`` backed by an AST object. Best effort is made to represent the object graph as children, interpreting
    common collections (e.g. dict, list, tuple, etc...) and common built-in values.
    """
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            value: Any,
            inline_comments: dict[int, str],  # Line to comment on that line
            block_comments: dict[int, str],  # Line to comment on that line
            empty_lines: set[int],
            max_lines: int
    ):
        """
        Construct a ``PythonAstNode`` object.

        :param parent: Attributes defining this node in relation to its parent, or ``None`` if this node has no parent
            (it represents root).
        :param value: Backing Python AST object, collection, or scalar type.
        """
        if value is None:
            value = Null()
        super().__init__(parent, value if type(value) in {bool, int, float, str, Null} else None)
        self._data = value
        self._inline_comments = inline_comments
        self._block_comments = block_comments
        self._empty_lines = empty_lines
        self._max_lines = max_lines

    def children(self) -> list[Node]:
        this = self._data
        ret = []

        def inject(label, value):
            if isinstance(value, ast.AST):
                p = SimpleNode(
                    ParentBlock(self, len(ret), label),
                    None
                )
                p.add_child(
                    PythonAstNode(
                        ParentBlock(p, 0, value.__class__.__name__),
                        value,
                        self._inline_comments,
                        self._block_comments,
                        self._empty_lines,
                        self._max_lines
                    )
                )
                p.seal()
                ret.append(p)
            else:
                ret.append(
                    PythonAstNode(
                        ParentBlock(self, len(ret), label),
                        value,
                        self._inline_comments,
                        self._block_comments,
                        self._empty_lines,
                        self._max_lines
                    )
                )

        if isinstance(this, dict):
            for i, k in enumerate(this.keys()):
                inject(k, this[k])
        elif isinstance(this, (list, tuple)):
            for i, v in enumerate(this):
                inject(i, v)
        elif isinstance(this, ast.AST):
            # inject('@type', this.__class__.__name__)
            # inject('@unparsed', ast.unparse(this))
            if hasattr(this, 'lineno') and getattr(this, 'lineno') is not None:
                line_idx = getattr(this, 'lineno')
                # Insert inline comment
                if line_idx in self._inline_comments:
                    inject('@comment_inline', self._inline_comments[line_idx])
                # Insert block comment before
                for i in range(line_idx-1, -1, -1):
                    if i in self._block_comments:
                        inject('@comment_before', self._block_comments[i])
                        break
                    if i not in self._empty_lines:
                        break
            if hasattr(this, 'end_lineno') and getattr(this, 'end_lineno') is not None:
                line_idx = getattr(this, 'end_lineno')
                # Insert block comment after
                for i in range(line_idx+1, self._max_lines):
                    if i in self._block_comments:
                        inject('@comment_after', self._block_comments[i])
                        break
                    if i not in self._empty_lines:
                        break
            for i, k in enumerate(k_ for k_ in dir(this) if not k_.startswith('_')):
                inject(k, getattr(this, k))
        return ret

    @staticmethod
    def create_root_path(code: str) -> PythonAstNode:
        """
        Equivalent to ``PythonAstNode(None, obj)``.

        :param code: Code to break down.
        :return: New ``PythonAstNode``.
        """
        code_lines = code.splitlines(keepends=True)
        # Pull empty lines
        empty_lines = {i+1 for i, l in enumerate(code_lines) if l.strip() == ''}
        # Pull inline comments
        code_lines_iter = iter(code_lines)
        tokens = tokenize.tokenize(lambda: next(code_lines_iter).encode('utf-8'))
        inline_comments = {}
        for token in tokens:
            if token.type == tokenize.COMMENT:
                start_line, start_col = token.start
                end_line, end_col = token.end
                inline_comments[start_line] = token.string
        # Pull block comments
        block_comment_active_text = ''
        block_comment_active_lines = []
        block_comments = {}
        for i, l  in enumerate(code_lines):
            l = l.strip()
            if l.startswith('#'):
                block_comment_active_text += l + '\n'
                block_comment_active_lines.append(i)
            else:
                if block_comment_active_text:
                    for i in block_comment_active_lines:
                        block_comments[i+1] = block_comment_active_text
                    block_comment_active_text = ''
                    block_comment_active_lines = []
        if block_comment_active_text:
            for i in block_comment_active_lines:
                block_comments[i+1] = block_comment_active_text
        # Parse tree
        parse_tree = ast.parse(code)
        return PythonAstNode(None, parse_tree, inline_comments, block_comments, empty_lines, len(code_lines))


if __name__ == '__main__':
    code = """
import numpy as np
import random  # hello world!
# hi!
  # bye!

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
random_numbers = [random.randint(1, 100) for _ in range(15)]
sorted_numbers = quicksort(random_numbers)
print(f"Sorted: {sorted_numbers}")

target = random.randint(1, 100)
index = binary_search(sorted_numbers, target)
if index != -1:
    print(f"Found {target} at index {index}.")
else:
    print(f"{target} not found.")

try:
    z = np.aaa.bbb.log(x / y)
except ArithmeticError:
    z = 0
    
x, y = 1, 2
"""
    path = PythonAstNode.create_root_path(code)
    for inner_path in path.descendants():
        print(f'{inner_path}')
    print(f'{isinstance(path, Node)}')