#!/usr/bin/env python

import argparse
import os
import logging
from .folder_parser import find_pdfs
from .pdf_searcher import PdfSearcher

logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', 
                        '--print_only', 
                        help='Do not perform any action on the pdf s. just print them out.',
                        action='store_true')
    parser.add_argument('-s', 
                        '--search_words', 
                        nargs='+', 
                        help='Enter flag "-s" followed by all the words you want to look for.',
                        required=True)
    args = parser.parse_args()
    
    top_folder = input_path(msg='The full path of the top folder: ')
    output = input('The full path of the output file: ')
    output_dir = input_path(folder=os.path.dirname(output))
    output = os.path.join(output_dir, os.path.basename(output))

    pdfs = find_pdfs(top_folder)
    if args.print_only:
        with open(output, 'w') as file:
            for pdf in pdfs:
                file.write(pdf + '\n')
                return
    
    print_progress_bar(0, len(pdfs))
    searcher = PdfSearcher(*list(args.search_words))
    for i, pdf in enumerate(pdfs, 1):
        try:
            searcher.search_pdf(pdf)
        except ValueError:
            logging.warning('Could not search {}'.format(pdf))
        print_progress_bar(i, len(pdfs))

    searcher.to_csv(output)

def input_path(folder=None, msg=''):
    if folder is None:
        folder = input(msg)
        input_path(folder)

    if not os.path.isdir(folder):
        folder = input('{} is not a valid folder, please correct: '.format(folder))
        input_path(folder)
    
    return folder

def print_progress_bar (iteration, 
                        total, 
                        prefix = 'Progress', 
                        suffix = 'Complete', 
                        decimals = 1, 
                        length = 50, 
                        fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

if __name__ == '__main__':
    main()