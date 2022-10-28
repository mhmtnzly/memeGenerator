"""
Base class for each file type.

Each file type is child of ingestor base class.
"""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class for each file type.
    """

    formats = ['csv', 'docx', 'pdf', 'txt']

    @classmethod
    def can_ingest(cls, path: str):
        """
        Determining the type of file.
        """
        path = path.split('.')[-1]
        return path in cls.formats

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """
        Parsing the file in the path and list returns of quote.
        """
        pass
