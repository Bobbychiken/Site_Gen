from enum import Enum 
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold" 
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self,other):
        return( self.text == other.text 
               and self.text_type == other.text_type 
               and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    if text_node.text_type == TextType.TEXT:
        text_node = LeafNode(tag=None,value=text_node.text)
        return text_node
    elif text_node.text_type == TextType.BOLD:
        text_node = LeafNode(tag='b',value=text_node.text)
        return text_node
    elif text_node.text_type == TextType.ITALIC:
        text_node = LeafNode(tag='i',value=text_node.text)
        return text_node
    elif text_node.text_type == TextType.CODE:
        text_node = LeafNode(tag='code',value=text_node.text)
        return text_node
    elif text_node.text_type == TextType.LINK:
        text_node = LeafNode(tag='a',value=text_node.text, props={"href":text_node.url})
        return text_node
    elif text_node.text_type == TextType.IMAGE:
        text_node = LeafNode(tag='img',value="",props={"src":text_node.url,"alt":text_node.text})
        return text_node
    else:
        raise Exception("somethign went wrong with text_type transition")
        
    