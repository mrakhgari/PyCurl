"""
This module contains the set of Requests' exceptions.
"""


class Error(Exception):
    """Base class for other exceptions"""

    def __init__(self, message):
        self.message = message


class InvalidUrl(Error):
    """Raised when the url is not valid"""

    def __init__(self, url):
        super().__init__(f"{url} is not valid")


class FileNotFound(Error):
    """Raised when file not found"""

    def __init__(self, file_path):
        super().__init__(f"Wrong file or file path, check the {file_path}")


class TimeOut(Error):
    """Raised when request timeouted"""

    def __init__(self, timeout):
        super().__init__(f"Time out ({timeout} s)")

class TwoDataType(Error):
    ''' Raised when user used --json and --data flag together'''
    def __init__(self):
        super().__init__("You can not use --data and --json together")