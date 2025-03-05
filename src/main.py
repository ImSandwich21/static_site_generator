import os
import shutil
from textnode import *
from markdown_blocks import *

def main():
    static_src = "static"
    public_dest = "public"

    print("Copying static files...")
    copy_static_files(static_src, public_dest)
    print("Static files copied successfully!")

def copy_static_files(src, dest):
    if os.path.exists(dest):
        print(f"Deleting existing directory: {dest}")
        shutil.rmtree(dest)

    os.makedirs(dest, exist_ok=True)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isdir(src_path): 
            print(f"Creating directory: {dest_path}")
            os.makedirs(dest_path, exist_ok=True)
            copy_static_files(src_path, dest_path) 
        else: 
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)

main()