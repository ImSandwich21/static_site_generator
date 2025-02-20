import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a test", None, None)
        node2 = HTMLNode("p", "This is a test", None, None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("p", "This is a test")
        node2 = HTMLNode("a", "This is a test")
        self.assertNotEqual(node, node2)

    def test_property_none(self):
        node = HTMLNode("h1", "This is a test")
        self.assertIsNone(node.props)

    def test_eq_leaf(self):
        node = LeafNode("a", "This is a test")
        node2 = LeafNode("a", "This is a test")
        self.assertEqual(node, node2)

    def test_eq_leaf_string(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_eq_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_eq_leaf_raw(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_no_value_leaf(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            print(node.to_html())

if __name__ == "__main__":
    unittest.main()