"""..."""
import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    """..."""
    def test_props_to_html(self):
        """..."""
        node = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"')

        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://google.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://google.com"',
        )


class TestLeafNode(unittest.TestCase):
    """..."""
    def test_to_html(self):
        """..."""
        node = LeafNode(
            tag="a",
            props={"href": "https://www.google.com"},
            value="Click me!"
            )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
            )

        node = LeafNode(
            tag="p",
            value="Click me!"
            )
        self.assertEqual(
            node.to_html(),
            '<p>Click me!</p>'
            )


if __name__ == "__main__":
    unittest.main()
