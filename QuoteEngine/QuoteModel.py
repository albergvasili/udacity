"""Ingest files that contain quotes."""


class QuoteModel():
    """Return quote body and author."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'
