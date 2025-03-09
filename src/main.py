import sys
import os
import shutil
from generate import copy_static_files, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_docs = "./docs"
template_path = "./template.html"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_static_files(dir_path_static, dir_path_docs)

    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

main()