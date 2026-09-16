from textnode import TextNode, TextType

def main():
    anchor_text = TextNode("some anchor text", TextType.LINK , "https://www.boot.dev")
    print(anchor_text)

if __name__ == "__main__":
    main()