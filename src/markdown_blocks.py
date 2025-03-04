import re
from enum import Enum
from htmlnode import (ParentNode, LeafNode)
from inline_markdown import (text_to_textnodes)
from textnode import (text_node_to_html)

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        final_blocks.append(block)
    return final_blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.ULIST
    
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html(text_node))
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                children_nodes.append(ParentNode("p", text_to_children(block)))

            case BlockType.HEADING:
                level = block.count("#", 0, block.index(" "))
                text = block[level + 1].strip()
                children_nodes.append(ParentNode(f"h{level}", text_to_children(text)))

            case BlockType.CODE:
                code_text = block[3:-3].strip() 
                code_node = ParentNode("pre", [ParentNode("code", [LeafNode(None, code_text)])])
                children_nodes.append(code_node)

            case BlockType.QUOTE:
                quote_text = "\n".join(line[1:].strip() for line in block.split("\n"))
                children_nodes.append(ParentNode("blockquote", text_to_children(quote_text)))

            case BlockType.ULIST:
                list_items = [ParentNode("li", text_to_children(line[2:].strip())) for line in block.split("\n")]
                children_nodes.append(ParentNode("ul", list_items))

            case BlockType.OLIST:
                list_items = [ParentNode("li", text_to_children(line[line.index(" ") + 1:].strip())) for line in block.split("\n")]
                children_nodes.append(ParentNode("ol", list_items))

            case _:
                raise Exception(f"Invalid BlockType: {block_type}")
            
            
    return ParentNode("div", children_nodes)