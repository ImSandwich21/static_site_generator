from textnode import *
from block_markdown import *

def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
    blocks = markdown_to_blocks(md)
    print(blocks)

main()