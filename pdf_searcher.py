import PyPDF2
import re
import csv
from collections import namedtuple 
Record = namedtuple('Record', 'file_path, word, page, occurence')

class PdfSearcher:
    """The pdf searcher is an object wich stores the desired search words but not the pdf and is as such
    designed to be used on multiple pdf's. It stores all found words in the pdf it has looked in 
    (using the search_pdf method) as records. A record contains info about: file path of the pdf,
    the word that was found, the page on which it was found and the amount of times it appeared on 
    that page."""

    def __init__(self, *args):
        """The positional arguments passed to initiliase the object are the search words it will use."""
        words = []
        for arg in args:
            words.append(arg.lower())
            words.append(arg.Upper())
            words.append(arg.Capitilize())
        self.search_words = [re.compile(word) for word in words]
        self.records = []

    def search_pdf(self, pdf_path):
        """Creates a record for each word found on each page. Scans the pdf file (passed through 
        with full path) and calls the match patterns method for each page. Each match that match_patterns
        returns is stored as a record in self.records."""
        with open(pdf_path, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extractText()
                for found in self.match_patterns(text):
                    self.records.append(Record(pdf_path, found[0], page_num, len(found)))

    def match_patterns(self, text):
        """Creates a generator that looks for all search words in a given text."""
        for word in self.search_words:
            match = word.findall(text)
            if match:
                yield match

    def to_csv(self, file_path, first=True):
        """Creates or appends a csv file containing all records that were found."""
        with open(file_path, 'a') as file:
            writer = csv.writer(file, dialect='excel', delimiter=",")
            if first:
                writer.writerow(['file_path', 'word', 'page', 'occurence'])
            for record in self.records:
                writer.writerow([record.file_path, record.word, record.page, record.occurence])
