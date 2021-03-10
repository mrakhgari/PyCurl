import argparse
import validators
from request import Request


class Error(Exception):
    """Base class for other exceptions"""

    def __init__(self, message):
        self.message = message


class InvalidUrl(Error):
    """Raised when the input value is too large"""

    def __init__(self, url):
        super().__init__(f"{url} is not valid")


def get_request(args: argparse.Namespace):
    url = args.url[0]
    
    if not validators.url(url):
        raise InvalidUrl(url)
    else:
        return Request(url)
