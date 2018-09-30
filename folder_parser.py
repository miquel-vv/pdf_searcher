import os
import logging

logging.basicConfig(filename='structure.txt', level=logging.DEBUG)

def find_pdfs(top_folder_path, print_only=True):
    """Walks through folder structure and calls the passed function on each pdf.
    Accepts the top file directory as first argument and a callback function as the second. The callback
    function should accept one argument: The pdf's absolute path."""
    pdf_list = []
    for top_folder, dirs, files in os.walk(top_folder_path):
        for file in files:
            name, file_type = os.path.splitext(os.path.join(top_folder,file))
            if file_type == '.pdf':
                pdf_list.append(os.path.join(top_folder,file))
    
    return pdf_list