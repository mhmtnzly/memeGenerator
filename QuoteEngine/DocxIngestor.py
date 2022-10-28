"""
It is quote ingestor for docx files.
"""

from .IngestorInterface import IngestorInterface, QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """
    It is a class for Docx Ingestor.
    In docx file the form must be body - author.
    """

    formats = ['docx']

    @classmethod
    def parse(cls, path: str):
        """
        If in the path is accepted format, parse it and return a list.
        """
        if cls.can_ingest(path):
            list_quotes = []
            file_docx = Document(path)
            for row in file_docx.paragraphs:
                line = row.text.split(' - ')
                if line[0] != '':
                    line_quote = QuoteModel(line[0], line[1])
                    list_quotes.append(line_quote)
        return list_quotes
