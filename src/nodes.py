from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: unmatched delimiter '{delimiter}' in text.")
        
        for i, part in enumerate(parts):
            if part:  # Ignore empty segments
                new_nodes.append(TextNode(part, text_type if i % 2 else TextType.TEXT))

    return new_nodes