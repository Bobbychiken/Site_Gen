import unittest
from textnode import TextNode, TextType
from nodesplitter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, Text_to_textnodes

class TestNodeSplitter(unittest.TestCase):


    def test_eq(self):
        node = TextNode("This is text with a 'code block' word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"'", TextType.CODE)

        self.assertEqual(
            new_nodes,[
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_bold(self):
        node = TextNode("We've got some *bold text* here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(
            new_nodes,[
                TextNode("We've got some ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
                TextNode(" here",TextType.TEXT),
            ]
        )


    def test_missing_delimiter_exception(self):
        node = TextNode("No delimiter here* and nothing to' seperate either`", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node],"'", TextType.CODE)

    def test_extracting_images(self):
        matches = extract_markdown_images(
            "This is totally not a rick roll ![Rick Roll](https://i.giphy.com/g7GKcSzwQfugw.webp)"
        )
        self.assertListEqual([("Rick Roll", "https://i.giphy.com/g7GKcSzwQfugw.webp")], matches)

    def test_extracting_links(self):
        matches = extract_markdown_links(
            "None of this text matters anyway, for the bit. [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is some silly text, and it doesn't matter. [to boot dev](https://www.boot.dev) More silly text. [another URL](https://www.google.com)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
                        [      
                            TextNode("This is some silly text, and it doesn't matter. ", TextType.TEXT),
                            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                            TextNode(" More silly text. ", TextType.TEXT),
                            TextNode("another URL", TextType.LINK, "https://www.google.com"),
                        ],
                        new_nodes,
                    )


    def text_Text_to_textnodes(self):
        node = TextNode(
            "'Here:' We have some _silly little_ text that *doesn't much matter*.[to boot dev](https://www.boot.dev). But don't yet be 'fooled' by the *text*. There is _more!_[google home](https://www.google.com) and a Rick Roll for good measure ![Rick Roll Gif](https://i.giphy.com/g7GKcSzwQfugw.webp)"
        )
        new_nodes = Text_to_textnodes([node.text])
        self.assertListEqual(
            [






                TextNode("Here:", TextType.CODE),
                TextNode("We have some ", TextType.TEXT),
                TextNode("silly little", TextType.ITALIC),
                TextNode(" text that ", TextType.TEXT),
                TextNode("doesn't much matter", TextType.BOLD),
                TextNode(".", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(". But don't yet be ", TextType.TEXT),
                TextNode("fooled", TextType.CODE),
                TextNode(" by the ", TextType.BOLD),
                TextNode(". There is ", TextType.TEXT),
                TextNode("more!", TextType.ITALIC),
                TextNode("google home", TextType.LINK, "https://www.google.com"),
                TextNode("and a Rick Roll for good measure ", TextType.TEXT),
                TextNode("Rick Roll Gif", TextType.IMAGE, "https://i.giphy.com/g7GKcSzwQfugw.webp"),
            ], 
            new_nodes
        )



  

if __name__ == "__main__":
    unittest.main()