"""..."""
import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    """..."""
    def test_eq(self):
        """..."""
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        """..."""
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        """..."""
        node = TextNode("This is a text node", "bold", None)
        self.assertIsNone(node.url)

    def test_equal_url(self):
        """..."""
        node = TextNode("This is a text node", "bold", "google.com")
        node2 = TextNode("This is a text node", "bold", "google.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
