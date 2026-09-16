import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode():
    def test_eq(self):
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
            props={"href": "https://www.goggle.com", "target": "_blank"}

        )
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello world")
        self.assertEqual(node.props_to_html(), "")   

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "this is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>this is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href":"https://www.goggle.com"})
        self.assertEqual(node.toHtml(), '<a href="https://www.google.com">Click me!<a/>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None,"Look at this raw text")
        self.assertEqual(node.to_html(), "Look at this raw text")



if __name__ =="__main__":
    unittest.main()