def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(filter(None, map(str.strip, blocks)))
    return blocks
