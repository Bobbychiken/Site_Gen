from enum import Enum
import re
from nodesplitter import markdown_to_blocks, Text_to_textnodes 
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    
    # 1. Heading: 1-6 '#' characters followed by a space
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
        
    # 2. Code block: starts with 3 backticks and ends with 3 backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
        
    # 3. Quote block: every line starts with '>'
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
        
    # 4. Unordered list: every line starts with '- '
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
        
    # 5. Ordered list: every line starts with an incrementing number followed by '. '
    is_ordered = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i + 1}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered and lines:
        return BlockType.ORDERED_LIST
        
    # 6. Default: Paragraph
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    incoming = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.CODE:
            codeblock = block.removeprefix("```\n")
            freshblock = codeblock.removesuffix("```")
            new_node = TextNode(freshblock, TextType.TEXT)
            textcode = text_node_to_html_node(new_node)
            middle = ParentNode("code", [textcode])
            outer = ParentNode("pre", [middle])
            incoming.append(outer)
        elif blocktype == BlockType.PARAGRAPH: 
            parablock = block.replace('\n', " ")
            para_node = text_to_children(parablock)
            node = ParentNode("p", para_node)
           
            incoming.append(node)
        elif blocktype == BlockType.HEADING: 
            hashes,headblock = block.split(" ",1)
            heading_node = text_to_children(headblock)
            node = ParentNode(f"h{len(hashes)}", heading_node)
            incoming.append(node)

        elif blocktype == BlockType.QUOTE: 
            lines = block.split("\n")
            cleaned = []
            for line in lines: 
                cleaned.append(line.removeprefix('> ').removeprefix('>'))
            quoteblock = " ".join(cleaned)
            quote_node = text_to_children(quoteblock)
            node = ParentNode("blockquote", quote_node)
            incoming.append(node)

        elif blocktype == BlockType.UNORDERED_LIST: 
            lines = block.split("\n")
            items = []
            for line in lines: 
                stripped= line.removeprefix("- ")
                items.append(ParentNode("li", text_to_children(stripped)))
            node = ParentNode("ul", items)
            incoming.append(node)

        elif blocktype == BlockType.ORDERED_LIST: 
            lines = block.split("\n")
            items = []
            for line in lines: 
                ol_line = line.split(" ",1)[1]
                items.append(ParentNode("li", text_to_children(ol_line)))
            node = ParentNode("ol", items)
            incoming.append(node)

    return  ParentNode("div", incoming)

def text_to_children(text):
    translation = Text_to_textnodes(text)
    children =[]
    for item in translation: 
        node = text_node_to_html_node(item)
        children.append(node)
    return children