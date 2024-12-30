from __future__ import annotations

import pathlib
from typing import Any

import bs4
from bs4 import BeautifulSoup

from xplore_path.paths.filesystem.file_loader import FileLoader, PATH_LOADER
from xplore_path.paths.filesystem.html_object_path import HtmlObjectPath


class HtmlFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.html'

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return HtmlObjectPath

    def load(self, p: pathlib.Path) -> Any:
        def html_to_dict_with_attributes(element):
            node = {}
            if element.attrs:
                for k, v in element.attrs.items():
                    node[f'@{k}'] = str(v)
            if list(element):
                for i, child in enumerate(element):
                    if isinstance(child, bs4.element.Tag):
                        node[i] = {child.name: html_to_dict_with_attributes(child)}
                    elif isinstance(child, (str, bs4.element.NavigableString)):
                        child = str(child).strip()
                        if child:
                            node[i] = child
                    else:
                        node[i] = child
            if element.string and element.string.strip():
                node['.text'] = element.string.strip()
            return node

        root = BeautifulSoup(p.read_bytes(), 'html.parser').html
        return {root.name: html_to_dict_with_attributes(root)}
