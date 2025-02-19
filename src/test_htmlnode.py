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

if __name__ == "__main__":
    unittest.main()