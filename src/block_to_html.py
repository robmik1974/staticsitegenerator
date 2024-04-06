"""..."""
import re
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode


from markdown_bloks import (
    markdown_to_blocks,
    block_to_block_type,
    BLOCK_TYPE_CODE,
    BLOCK_TYPE_HEADING,
    BLOCK_TYPE_ORDERED_LIST,
    BLOCK_TYPE_PARAGRAPH,
    BLOCK_TYPE_QUOTE,
    BLOCK_TYPE_UNORDERED_LIST
)


def text_to_children(text):
    """Creates blok of documents for each html node"""
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        html_node = text_node_to_html_node(textnode)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    """Converts paragraph block into html node"""
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(blok):
    """Converst heading block into html node"""
    level = 0
    for char in blok:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(blok):
        raise ValueError(f"Invalid heading level: {level}")
    text = blok[level+1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    """Converts code block into html node"""
    if not re.match(r"^`{3}\n.*\n`{3}$", block):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    """Converst quote block into html node"""
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not re.match(r"^>", line):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    """Converst unordered list into html node"""
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def ordered_list_to_html_node(block):
    """Convert ordered list into html node"""
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def markdown_to_html_node(markdown):
    """Converts a full markdown document into HMTL node """
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    """Invokes converting function based on type of block"""
    block_type = block_to_block_type(block)
    if block_type == BLOCK_TYPE_PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BLOCK_TYPE_HEADING:
        return heading_to_html_node(block)
    if block_type == BLOCK_TYPE_CODE:
        return code_to_html_node(block)
    if block_type == BLOCK_TYPE_ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_type == BLOCK_TYPE_UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BLOCK_TYPE_QUOTE:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")
