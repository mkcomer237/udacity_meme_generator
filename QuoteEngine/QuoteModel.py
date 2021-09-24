"""Simple class to encapsulate Quote data."""


class QuoteModel():
    """Simple class to encapsulate Quote data.

    Takes the quotation body and author as inputs and
    stores these as class attributes.
    """

    def __init__(self, author, body):
        """Initialize the class attributes."""
        self.author = author
        self.body = body

    def __str__(self):
        """Overwrite the str method for more helpful printing."""
        return f'A quotation by {self.author} that says "{self.body}"'

    def __repr__(self):
        """Overwrite how the object is represented to show the contents."""
        return f'<{self.author}, {self.body}>'
