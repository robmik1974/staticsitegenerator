"""..."""
from textnode import(
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Converts a raw string into a list of TextNode objects"""
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(old_node)
            continue
        nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")
        for index, value in enumerate(sections):
            if value == "":
                continue
            if index % 2 == 0:
                nodes.append(TextNode(text=value, text_type=TEXT_TYPE_TEXT))
            else:
                nodes.append(TextNode(text=value, text_type=text_type))
        new_nodes.extend(nodes)
    return new_nodes
