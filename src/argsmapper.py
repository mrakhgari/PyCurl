import argparse
import validators
from request import Request
from exceptions import InvalidUrl
import logging


def parse_headers(headers_list: list):
    if headers_list is None:
        return None
    headers_dict = {}
    for items in headers_list:
        for header in items.split(','):
            key, value = map(str, header.split(':'))
            if headers_dict.get(key) is not None:
                logging.warning(f"HeaderWarning:The {key} is exists, we override it by {value}")
            headers_dict[key] = value
    return headers_dict


def get_request(args: argparse.Namespace):
    url = args.url[0]
    method = args.method
    headers = parse_headers(args.header)
    if not validators.url(url):
        raise InvalidUrl(url)

    return Request(url, method, headers=headers)
