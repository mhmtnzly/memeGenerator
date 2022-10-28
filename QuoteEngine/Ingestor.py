"""
It is used that encapsulate modules for different types of files.
"""
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    """
    Encapsulate class for each type of file.
    """

    formats = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str):
        """
        It parses all files that given.
        """
        for types in cls.formats:
            if types.can_ingest(path):
                return types.parse(path)
