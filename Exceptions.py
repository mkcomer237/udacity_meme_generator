"""Custom exceptions to handle file errors."""


class InvalidFileFormat(Exception):
    """Use for unsupported file formats."""

    pass


class InvalidImageSize(Exception):
    """Use if the source image is too small."""

    pass


class InvalidTextInput(Exception):
    """Use when text is too long."""

    pass
