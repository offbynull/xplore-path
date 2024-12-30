from __future__ import annotations

import pathlib
from typing import Any
from xml.etree import ElementTree

from xplore_path.paths.filesystem.file_loader import FileLoader, PATH_LOADER
from xplore_path.paths.filesystem.xml_object_path import XmlObjectPath


class XmlFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.xml'

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return XmlObjectPath

    def load(self, p: pathlib.Path) -> Any:
        def xml_to_dict_with_attributes(element):
            node = {}
            for k, v in element.attrib.items():
                node[f'@{k}'] = v
            if list(element):
                node |= {i: {child.tag: xml_to_dict_with_attributes(child)} for i, child in enumerate(element)}
            elif element.text and element.text.strip():
                node['.text'] = element.text.strip()
            return node

        root = ElementTree.parse(p).getroot()
        return {root.tag: xml_to_dict_with_attributes(root)}
