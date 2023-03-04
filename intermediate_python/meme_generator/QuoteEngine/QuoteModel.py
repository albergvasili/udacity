"""Ingest files that contain quotes."""


class QuoteModel():
    """Return quote body and author."""

    def __init__(self, body, author):
        """Assign body and author variables to the self object."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return body and author of the quote."""
        return f'"{self.body}" - {self.author}'
