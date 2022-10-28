"""
It is quote ingestor for csv files.
"""

from .IngestorInterface import IngestorInterface, QuoteModel
from pandas import read_csv


class CSVIngestor(IngestorInterface):
    """
    It is a class for Csv Ingestor.
    In Csv file the form must be body - author.
    """

    formats = ['csv']

    @classmethod
    def parse(cls, path: str):
        """
        If in the path is accepted format, parse it and return a list.
        """
        if cls.can_ingest(path):
            list_quotes = []
            csv_file = read_csv(path)
            for row in range(len(csv_file)):
                line_quote = QuoteModel(
                    csv_file.iloc[row]['body'], csv_file.iloc[row]['author'])
                list_quotes.append(line_quote)
        return list_quotes
