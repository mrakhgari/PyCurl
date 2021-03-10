import argparse
import validators
from request import Request
from exceptions import InvalidUrl
import logging


def parse_headers(headers_list: list):
    if headers_list is None:
        return None
    headers_list = ','.join(headers_list)
    headers_dict = {}
    for header in headers_list.split(','):
        key, value = map(str, header.split(':'))
        if headers_dict.get(key) is not None:
            logging.warning(
                f"HeaderWarning:The {key} is exists, we override it by {value}")
        headers_dict[key] = value
    return headers_dict


def parse_queries(queries_list: list):
    if queries_list is None:
        return None
    queries_dict: dict = {}
    queries_list = '&'.join(queries_list)
    for query in queries_list.split('&'):
        key, value = map(str, query.split('='))
        if queries_dict.get(key) is not None:
            logging.warning(
                f"QueryWarning:The {key} is exists, we override it by {value}")
        queries_dict[key] = value
    return queries_dict


def parse_data(data: str, headers: dict):
    import re
    query_string_pattern = r"(\w+=\w+&?)+"
    if not re.fullmatch(query_string_pattern, data):
        logging.warning(f"DataPattern: Your provided information is not of type x-www-form-urlencoded")
    if headers.get("Content-Type") is None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    return data


def get_request(args: argparse.Namespace):
    url = args.url[0]
    method = args.method
    headers = parse_headers(args.header)
    queries = parse_queries(args.queries)
    data = parse_data(args.data, headers)
    if not validators.url(url):
        raise InvalidUrl(url)

    return Request(url, method, headers=headers, queries=queries, data=data)
