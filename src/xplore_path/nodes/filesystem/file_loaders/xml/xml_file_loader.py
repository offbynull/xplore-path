from __future__ import annotations

import pathlib
from typing import Any
from xml.etree import ElementTree

from xplore_path.nodes.filesystem.file_loader import FileLoader, NODE_CREATOR
from xplore_path.nodes.filesystem.file_loaders.xml._xml_object_node import XmlObjectNode, XmlTag


class XmlFileLoader(FileLoader):
    """
    ``FileLoader`` for XML files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.xml'

    def node_creator(self, p: pathlib.Path) -> NODE_CREATOR:
        return XmlObjectNode

    def load(self, p: pathlib.Path) -> Any:
        def xml_to_tags(element):
            attrs = {}
            text = None
            values = []
            for k, v in element.attrib.items():
                attrs[f'@{k}'] = str(v)
            if list(element):
                values = [xml_to_tags(child) for child in element]
            elif element.text and element.text.strip():
                text = element.text.strip()
            return XmlTag(element.tag, attrs, text, values)

        root = ElementTree.parse(p).getroot()
        return xml_to_tags(root)
