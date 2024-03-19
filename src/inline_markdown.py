"""..."""
import re
from textnode import(
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
    TEXT_TYPE_IMAGE,
    TEXT_TYPE_LINK
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


def extract_markdown_images(text):
    """Extracts imgaes from text using patterns"""
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    """Extracts links from text using patterns"""
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    """Converts a TextNode text into a list of TextNode objects extracting images"""
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(image[0], TEXT_TYPE_IMAGE, image[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TEXT_TYPE_TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    """Converts a TextNode text into a list of TextNode objects extracting links"""
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(link[0], TEXT_TYPE_LINK, link[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TEXT_TYPE_TEXT))
    return new_nodes
