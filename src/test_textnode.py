"""..."""
import unittest
from textnode import (
    TextNode,
    TEXT_TYPE_BOLD,
    # TEXT_TYPE_CODE,
    # TEXT_TYPE_IMAGE,
    TEXT_TYPE_ITALIC,
    # TEXT_TYPE_LINK,
    TEXT_TYPE_TEXT
)


class TestTextNode(unittest.TestCase):
    """..."""
    def test_eq(self):
        """..."""
        node = TextNode("This is a text node", TEXT_TYPE_BOLD)
        node2 = TextNode("This is a text node", TEXT_TYPE_BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        """..."""
        node = TextNode("This is a text node", TEXT_TYPE_BOLD)
        node2 = TextNode("This is a text node", TEXT_TYPE_ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        """..."""
        node = TextNode("This is a text node", TEXT_TYPE_TEXT)
        node2 = TextNode("This is a text node2", TEXT_TYPE_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        """..."""
        node = TextNode("This is a text node", TEXT_TYPE_BOLD, None)
        self.assertIsNone(node.url)

    def test_equal_url(self):
        """..."""
        node = TextNode("This is a text node", TEXT_TYPE_TEXT, "google.com")
        node2 = TextNode("This is a text node", TEXT_TYPE_TEXT, "google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        """..."""
        node = TextNode("This is a text node",
                        TEXT_TYPE_BOLD,
                        "https://www.google.com")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.google.com)",
            repr(node)
            )


if __name__ == "__main__":
    unittest.main()
