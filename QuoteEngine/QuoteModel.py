"""
It is containing QuoteModel class.
"""


class QuoteModel:
    """
    Defining th quote model text.
Attributes:
    body: str - it is quote text
    author: str - it is the name of quote's author
    """

    def __init__(self, body, author):
        """
        Initilizes of a quote to generate the object.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """
        Represent the object.
        """
        return f'{self.body} {self.author}'
