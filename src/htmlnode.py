



class HTMLNode():
    def __init__(self,tag = None,value = None ,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self,other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")


    def props_to_html(self):
        if not self.props:
            return ""


        attributes =[]
        for key,val in self.props.items():
            attributes.append(f' {key}="{val}"')
        return "".join(attributes)


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,value=None,children=children,props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node in need of a tag")
        if self.children is None: 
            raise ValueError("All parent nodes must have a child.")
        parent_list = []
        for child in self.children:
            parent_list.append(child.to_html())
        return f"<{self.tag}{self.props_to_html()}>{''.join(parent_list)}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.children},{self.props})"
