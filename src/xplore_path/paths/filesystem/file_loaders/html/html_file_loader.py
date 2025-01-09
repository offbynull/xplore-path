from __future__ import annotations

import pathlib
from typing import Any

import bs4
from bs4 import BeautifulSoup

from xplore_path.paths.filesystem.file_loader import FileLoader, PATH_LOADER
from xplore_path.paths.filesystem.file_loaders.xml.xml_object_path import XmlObjectPath, XmlTag


class HtmlFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.html'

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return XmlObjectPath

    def load(self, p: pathlib.Path) -> Any:
        def html_to_tags(element):
            attrs = {}
            text = None
            values = []
            if element.attrs:
                for k, v in element.attrs.items():
                    attrs[f'@{k}'] = str(v)
            if list(element):
                for child in element:
                    if isinstance(child, bs4.element.Tag):
                        values.append(html_to_tags(child))
                    # elif isinstance(child, (str, bs4.element.NavigableString)):
                    #     child = str(child).strip()
                    #     if child:
                    #         node[i] = child
                    # else:
                    #     node[i] = child
            if element.string and element.string.strip():
                text = element.string.strip()
            return XmlTag(element.name, attrs, text, values)

        root = BeautifulSoup(p.read_bytes(), 'html.parser').html
        return html_to_tags(root)
