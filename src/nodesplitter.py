from textnode import TextNode, TextType

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
