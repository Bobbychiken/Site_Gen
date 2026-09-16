import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        node3 = TextNode("text of my own making", TextType.ITALIC, None)
        node4 = TextNode("Text of my own making", TextType.ITALIC)
        self.assertEqual(node,node2)
        self.assertEqual(node3,node4)
        self.assertNotEqual(node,node3)

if __name__ =="__main__":
    unittest.main()