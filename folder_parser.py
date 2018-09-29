import os
import logging

logging.basicConfig(filename='structure.txt', level=logging.DEBUG)

def find_pdfs(top_folder_path, fn):
    """Walks through folder structure and calls the passed function on each pdf.
    Accepts the top file directory as first argument and a callback function as the second. The callback
    function should accept one argument: The pdf's absolute path."""
    for top_folder, dirs, files in os.walk(top_folder_path):
        for file in files:
            name, file_type = os.path.splitext(os.path.join(top_folder,file))
            if file_type == '.pdf':
                fn(os.path.join(top_folder,file))
                logging.info(os.path.join(top_folder,file))
