from enum import Enum
import re

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