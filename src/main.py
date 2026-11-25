import os
import shutil
from textnode import TextNode, TextType
from block_markdown import markdown_to_html_node, extract_title

def copy_static_to_public(source: str, target: str) -> None:
    if os.path.exists(target):
        shutil.rmtree(target)
    os.makedirs(target,exist_ok =True)
    copy_recursive(source, target)

def copy_recursive(source, target): 
    os.makedirs(target, exist_ok=True)
    for entry in os.listdir(source):
        src_path = os.path.join(source, entry)
        tar_path = os.path.join(target, entry)
        if os.path.isfile(src_path):
            shutil.copy(src_path, tar_path)
            print(f"Copied: {src_path} -> {tar_path}")
        elif os.path.isdir(src_path):
            copy_recursive(src_path, tar_path)
def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as s:
        source = s.read()
    with open(template_path, "r", encoding="utf-8") as m:
        model = m.read()
    content_html = markdown_to_html_node(source).to_html()
    title = extract_title(source)
    page_html = model.replace("{{ Title }}", title).replace("{{ Content }}", content_html) 
    dest_dir = os.path.dirname(dest_path)
    if dest_dir: 
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, 'w', encoding="utf-8") as d: 
        d.write(page_html)



def main():
    #anchor_text = TextNode("some anchor text", TextType.LINK , "https://www.boot.dev")
    #print(anchor_text)
    copy_static_to_public("static","public")
    generate_page("content/index.md","template.html","public/index.html")
if __name__ == "__main__":
    main()