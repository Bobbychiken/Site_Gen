import unittest
from textnode import TextNode, TextType
from nodesplitter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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




    def test_extraction_links(self): 
        pass

if __name__ == "__main__":
    unittest.main()