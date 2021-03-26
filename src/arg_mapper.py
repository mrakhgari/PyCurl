import argparse
import validators
from request import Request
from exceptions import InvalidUrl, FileNotFound
import logging
from constants import *
import json


def parse_headers(headers_list: list):
    if headers_list is None:
        return {}
    headers_list = ','.join(headers_list)
    headers_dict = {}
    for header in headers_list.split(','):
        key, value = map(str, header.split(':'))
        key = key.lower()
        if headers_dict.get(key) is not None:
            logging.warning(header_pattern_warning.format(key=key, value=value))
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
            logging.warning(query_pattern_warning.format(key=key, value=value))
        queries_dict[key] = value
    return queries_dict


def parse_data(data: str, headers: dict):
    if data is None:
        return
    import re
    query_string_pattern = r"(\w+=\w+)(&\w+=\w+)*"
    if not re.fullmatch(query_string_pattern, data):
        logging.warning(data_pattern_warning)
    if headers.get(content_type) is None:
        headers[content_type] = data_header
    return data


def parse_json(j: str, headers: dict):
    if j is None:
        return None
    if headers.get(content_type) is None:
        headers[content_type] = json_header
    try:
        json.loads(j)
        return json.loads(j)
    except ValueError as e:
        logging.warning(json_pattern_warning)
    return j


def parse_file(file: str, headers: dict):
    if file is None:
        return None
    file_name, file_path = map(str, file.split(":"))
    try:
        f = open(file_path, "rb")
    except:
        raise FileNotFound(file_path)
    if headers.get(content_type) is None:
        headers[content_type] = octet_header
    return {file_name: f}


def get_request(args: argparse.Namespace):
    url = args.url[0]
    if not validators.url(url):
        raise InvalidUrl(url)

    method = args.method
    timeout = args.timeout
    headers = parse_headers(args.header)
    queries = parse_queries(args.queries)
    data = parse_data(args.data, headers)
    json = parse_json(args.json, headers)
    file = parse_file(args.file, headers)

    return Request(url, method, headers=headers, queries=queries, data=data, json=json, file=file, timeout=timeout)
