import unittest
from textnode import TextType, TextNode,text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        node3 = TextNode("text of my own making", TextType.ITALIC, None)
        node4 = TextNode("text of my own making", TextType.ITALIC)
        self.assertEqual(node,node2)
        self.assertEqual(node3,node4)
        self.assertNotEqual(node,node3)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        bold_node = TextNode("This is meant to be bold!", TextType.BOLD)
        html_boldnode = text_node_to_html_node(bold_node)
        self.assertEqual(html_boldnode.tag, 'b')
        self.assertEqual(html_boldnode.value, "This is meant to be bold!")

        italic_node = TextNode("This is wiggly!", TextType.ITALIC)
        html_inode = text_node_to_html_node(italic_node)
        self.assertEqual(html_inode.tag, 'i')
        self.assertEqual(html_inode.value, "This is wiggly!")

        code_node = TextNode("y=mx+b", TextType.CODE)
        h_code_node = text_node_to_html_node(code_node)
        self.assertEqual(h_code_node.tag,"code")
        self.assertEqual(h_code_node.value,"y=mx+b")

        link_node = TextNode("This is a link to Google!", TextType.LINK, "https://www.google.com")
        h_link_node = text_node_to_html_node(link_node)
        self.assertEqual(h_link_node.tag, 'a')
        self.assertEqual(h_link_node.value, "This is a link to Google!")
        self.assertEqual(h_link_node.props, {"href": "https://www.google.com"})

        image_node = TextNode("This is a glorious image", TextType.IMAGE, "https://www.google.com")
        html_image_node = text_node_to_html_node(image_node)
        self.assertEqual(html_image_node.tag, 'img')
        self.assertEqual(html_image_node.value, "")
        self.assertEqual(html_image_node.props, {"src":"https://www.google.com", "alt": "This is a glorious image"})

        false_node = TextNode("all wrong, this is all wrong", "TextType.TEXT")
        with self.assertRaises(Exception):
            text_node_to_html_node(false_node)
        



if __name__ =="__main__":
    unittest.main()