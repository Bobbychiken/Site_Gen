import os
import shutil
import sys
from pathlib import Path
from textnode import TextNode, TextType
from block_markdown import markdown_to_html_node, extract_title

def copy_static_to_docs(source: str, target: str) -> None:
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

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as s:
        source = s.read()
    with open(template_path, "r", encoding="utf-8") as m:
        model = m.read()
    content_html = markdown_to_html_node(source).to_html()
    title = extract_title(source)
    #print(f"{title}")
    page_html = (model.replace("{{ Title }}", title)
        .replace("{{ Content }}", content_html)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
                 
                 )
    dest_dir = os.path.dirname(dest_path)
    if dest_dir: 
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, 'w', encoding="utf-8") as d: 
        d.write(page_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    md_dir_paths = os.listdir(dir_path_content)
    for entry in md_dir_paths:
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, Path(dest_path).with_suffix(".html"), basepath)
                          
        else:
            generate_pages_recursive(from_path,template_path,dest_path, basepath)



def main():
    basepath = sys.argv[1] if len(sys.argv)> 1 else "/"
    #anchor_text = TextNode("some anchor text", TextType.LINK , "https://www.boot.dev")
    #print(anchor_text)
    copy_static_to_docs("static","docs")
    generate_pages_recursive("content","template.html","docs", basepath)
if __name__ == "__main__":
    main()