import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def tets_eq(self):
        node = HTMLNode("a", "Click here", props={"href":"https://www.google.com"})
        node2 = HTMLNode("a", "Click here", props={"href":"https://www.google.com"})
        node3 = HTMLNode("b", "Push this", props={"href":"https://www.google.com"})
        node4 = HTMLNode("b", "Push this", props={"href":"https://www.google.com"})
        self.assertEqual(node,node2)
        self.assertEqual(node3,node4)
        self.assertNotEqual(node,node3)

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            "b",
            "Click here",
            props={"href": "https://www.google.com", "target": "_blank"}

        )
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.props_to_html(), "")   

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "this is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>this is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None,"Look at this raw text")
        self.assertEqual(node.to_html(), "Look at this raw text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

        child_node2 = LeafNode("saber", "child")
        parent_node2 = ParentNode("jedi", [child_node2])
        self.assertNotEqual(parent_node2.to_html(), "<saber><jedi>child</jedi></saber>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

        grandchild_node2 = LeafNode("anakin", "grandchild")
        child_node2 = ParentNode("palpatine", [grandchild_node2])
        midchild_node2 = ParentNode("obi-wan", [grandchild_node2])
        parent_node2 = ParentNode("Mortis",[child_node2,midchild_node2])
        self.assertEqual(
            parent_node2.to_html(), "<Mortis><palpatine><anakin>grandchild</anakin></palpatine><obi-wan><anakin>grandchild</anakin></obi-wan></Mortis>"
        )



if __name__ =="__main__":
    unittest.main()