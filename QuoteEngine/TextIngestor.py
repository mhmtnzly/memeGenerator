"""
It is quote ingestor for txt files.
"""

from .IngestorInterface import IngestorInterface, QuoteModel


class TextIngestor(IngestorInterface):
    """
    It is a class for Txt Ingestor.
    In txt file the form must be body - author.
    """

    formats = ['txt']

    @classmethod
    def parse(cls, path: str):
        """
        If in the path is accepted format, parse it and return a list.
        """
        if cls.can_ingest(path):
            list_quotes = []
            with open(path, 'r') as file:
                for row in file:
                    line = row.split(' - ')
                    line_quote = QuoteModel(line[0], line[1])
                    list_quotes.append(line_quote)
        return list_quotes
