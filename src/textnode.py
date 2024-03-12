"""..."""
from htmlnode import LeafNode


TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"


class TextNode:
    """..."""
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        return (
            self.text == text_node.text
            and self.text_type == text_node.text_type
            and self.url == text_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    """..."""
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(tag=None, value=text_node.text)
    if text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode(tag="a", value=text_node.text,
                        props={"href": text_node.url})
    if text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode(tag="img", value="",
                        props={"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"{text_node.text_type} is not supported type")
