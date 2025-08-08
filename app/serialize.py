import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.books import Book


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


def get_serialize_strategy(serialize_type: str) -> SerializeStrategy:
    if serialize_type == "json":
        return JsonSerialize()
    elif serialize_type == "xml":
        return XmlSerialize()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")
