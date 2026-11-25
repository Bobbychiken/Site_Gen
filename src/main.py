import os
import shutil
from textnode import TextNode, TextType

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



def main():
    #anchor_text = TextNode("some anchor text", TextType.LINK , "https://www.boot.dev")
    #print(anchor_text)
    copy_static_to_public("static","public")
if __name__ == "__main__":
    main()