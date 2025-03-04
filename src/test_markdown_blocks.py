import unittest
from markdown_blocks import (
    BlockType,
    markdown_to_blocks, 
    block_to_block_type, 
    markdown_to_html_node)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_heading(self):
        md = "# This is a heading"

        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_block_to_paragraph(self):
        md = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."

        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_unordered_list(self):
        md = """- This is the first list item in a list block
- This is a list item
- This is another list item"""

        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.ULIST, block_type)

    def test_block_to_ordered_list(self):
        md = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""

        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.OLIST, block_type)

