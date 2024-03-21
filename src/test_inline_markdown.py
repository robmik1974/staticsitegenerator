"""..."""
import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes

)
from textnode import (
    TextNode,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_CODE,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_IMAGE,
    TEXT_TYPE_LINK
    )


class TestInlineMarkdown(unittest.TestCase):
    """Test convertion a raw string into a list of TextNode objects"""
    def test_delimiter_bold(self):
        """Test conversion a raw string with single bold text"""
        node = TextNode("This is text with a **bold text** word",
                        TEXT_TYPE_TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD),
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT, None),
                TextNode("bold text", TEXT_TYPE_BOLD, None),
                TextNode(" word", TEXT_TYPE_TEXT, None)
            ]
            )

    def test_delimiter_bold_double(self):
        """Test conversion a raw string with double bold text"""
        node = TextNode(
            "This is text with a **bold text** word and **bold text** word",
            TEXT_TYPE_TEXT
            )
        self.assertListEqual(
            split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD),
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT, None),
                TextNode("bold text", TEXT_TYPE_BOLD, None),
                TextNode(" word and ", TEXT_TYPE_TEXT, None),
                TextNode("bold text", TEXT_TYPE_BOLD, None),
                TextNode(" word", TEXT_TYPE_TEXT, None)
            ]
            )

    def test_delimiter_italic(self):
        """Test conversion a raw string with italic text"""
        node = TextNode("This is text with a *italic text* word",
                        TEXT_TYPE_TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "*", TEXT_TYPE_ITALIC),
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT, None),
                TextNode("italic text", TEXT_TYPE_ITALIC, None),
                TextNode(" word", TEXT_TYPE_TEXT, None)
            ]
        )

    def test_delimiter_code(self):
        """Test conversion a raw string with code block"""
        node = TextNode("This is text with a `code block` word",
                        TEXT_TYPE_TEXT)
        self.assertListEqual(
            split_nodes_delimiter([node], "`", TEXT_TYPE_CODE),
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT, None),
                TextNode("code block", TEXT_TYPE_CODE, None),
                TextNode(" word", TEXT_TYPE_TEXT, None)
            ]
        )

    def test_extract_markdown_images(self):
        """Test extracting imgages from text using patterns"""
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        self.assertListEqual(
            extract_markdown_images(text=text),
            [('image', 'https://i.imgur.com/zjjcJKZ.png')]
        )

    def test_extract_markdown_links(self):
        """Test extracting links from text using patterns """
        text = "This is text with a [link](https://www.example.com)\
            and [another](https://www.example.com/another)"
        self.assertListEqual(
            extract_markdown_links(text=text),
            [('link', 'https://www.example.com'),
             ('another', 'https://www.example.com/another')]
        )

    def test_split_image(self):
        """Tests spliting nodes by included imgage using patterns"""
        node_text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        node = TextNode(
            node_text,
            TEXT_TYPE_TEXT)
        self.assertListEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", TEXT_TYPE_TEXT),
                TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ]
        )

    def test_split_image_single(self):
        """Tests spliting nodes by included sigle imgage using patterns"""
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            TEXT_TYPE_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TEXT_TYPE_IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        """Tests spliting nodes by included imgages using patterns"""
        node_text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        node_text += " and another ![second image](https://i.imgur.com/3elNhQu.png)"
        node = TextNode(
            node_text,
            TEXT_TYPE_TEXT)
        self.assertListEqual(
            split_nodes_image([node]),
            [
                TextNode("This is text with an ", TEXT_TYPE_TEXT),
                TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TEXT_TYPE_TEXT),
                TextNode("second image", TEXT_TYPE_IMAGE, "https://i.imgur.com/3elNhQu.png")
            ]
        )

    def test_split_link(self):
        """Tests spliting nodes by included link using patterns"""
        node_text = "This is text with a [link](https://www.example.com)"
        node = TextNode(
            node_text,
            TEXT_TYPE_TEXT)
        self.assertListEqual(
            split_nodes_link([node]),
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("link", TEXT_TYPE_LINK, "https://www.example.com")
            ]
        )

    def test_split_links(self):
        """Tests spliting nodes by included links using patterns"""
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TEXT_TYPE_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("link", TEXT_TYPE_LINK, "https://boot.dev"),
                TextNode(" and ", TEXT_TYPE_TEXT),
                TextNode("another link", TEXT_TYPE_LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TEXT_TYPE_TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        """Tests converting inline markdown into list of Text Nodes"""
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TEXT_TYPE_TEXT),
                TextNode("text", TEXT_TYPE_BOLD),
                TextNode(" with an ", TEXT_TYPE_TEXT),
                TextNode("italic", TEXT_TYPE_ITALIC),
                TextNode(" word and a ", TEXT_TYPE_TEXT),
                TextNode("code block", TEXT_TYPE_CODE),
                TextNode(" and an ", TEXT_TYPE_TEXT),
                TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TEXT_TYPE_TEXT),
                TextNode("link", TEXT_TYPE_LINK, "https://boot.dev"),
            ],
            nodes,
        )
