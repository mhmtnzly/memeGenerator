"""
It is quote ingestor for pdf files.
"""

from .IngestorInterface import IngestorInterface, QuoteModel
import subprocess
import random
import os


class PDFIngestor (IngestorInterface):
    """
    It is a class for PDF Ingestor.
    In PDF file the form must be body - author.
    """

    formats = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """
        If in the path is accepted format, parse it and return a list.
        """
        if cls.can_ingest(path):
            list_quotes = []
            tmp = f'./tmp_{random.randint(0,1000000)}.txt'
            subprocess.run(['pdftotext', '-layout', path, tmp])
            with open(tmp, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line != '':
                        line.split(' - ')
                        quote = QuoteModel(line[0], line[1])
                        list_quotes.append(quote)
            os.remove(tmp)
            return list_quotes
