"""..."""
import unittest
from markdown_bloks import markdown_to_blocks
from markdown_bloks import block_to_block_type

from markdown_bloks import (
    BLOCK_TYPE_CODE,
    BLOCK_TYPE_HEADING,
    BLOCK_TYPE_ORDERED_LIST,
    BLOCK_TYPE_PARAGRAPH,
    BLOCK_TYPE_QUOTE,
    BLOCK_TYPE_UNORDERED_LIST,
)


class TestMarkdownToHTML(unittest.TestCase):
    """Test spliting document into sections beased on patterns"""
    def test_markdown_blocks(self):
        """..."""
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertListEqual(
            markdown_to_blocks(md),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        """..."""
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


class TestBlockType(unittest.TestCase):
    """Class represenating tests related to types of markdown"""
    def test_block_to_blok_type(self):
        """Test makdown blokc type beased on patterns"""
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_QUOTE)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BLOCK_TYPE_PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
