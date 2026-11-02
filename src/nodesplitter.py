from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes =[]
    split_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter) 
        if len(sections) % 2 ==0: 
            raise Exception("Invalid Markdown syntac: Missing delimieter")

        for i in range(len(sections)): 
            if sections[i] =="":
                continue
            if i % 2 ==0: 
                new_nodes.append(TextNode(sections[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes: 
        if node.text_type != TextType.TEXT:
                    new_nodes.append(node)
                    continue
        remaining_text = node.text
        extracted = extract_markdown_images(remaining_text)
        
        while extracted:
            alt, url = extracted[0]
            before, after = remaining_text.split(f"![{alt}]({url})",1 )
            new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining_text = after
            extracted = extract_markdown_images(remaining_text)
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode])-> list[TextNode]:
    new_nodes = []
    for node in old_nodes: 
        if node.text_type != TextType.TEXT:
                    new_nodes.append(node)
                    continue
        remaining_text = node.text
        extracted = extract_markdown_links(remaining_text)
        
        while extracted:
            alt, url = extracted[0]
            before, after = remaining_text.split(f"[{alt}]({url})",1 )
            new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            remaining_text = after
            extracted = extract_markdown_links(remaining_text)
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(input_text: str)-> list:
    img_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    extracted_images = re.findall(img_pattern,input_text)

    return extracted_images

def extract_markdown_links(input_text: str)-> list:
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    extracted_links = re.findall(link_pattern, input_text)

    return extracted_links

