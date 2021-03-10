
class Error(Exception):
    """Base class for other exceptions"""

    def __init__(self, message):
        self.message = message


class InvalidUrl(Error):
    """Raised when the url is not valid"""

    def __init__(self, url):
        super().__init__(f"{url} is not valid")
