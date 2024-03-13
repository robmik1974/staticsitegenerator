"""..."""
import unittest

from inline_markdown import split_nodes_delimiter
from textnode import (
    TextNode,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_CODE,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_TEXT
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
