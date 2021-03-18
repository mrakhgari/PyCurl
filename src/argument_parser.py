"""Command-line parsing module

This module is an optparse-inspired command-line parsing library that
use from argparse to parse the arguments.
"""
import argparse
from constants import *


def get_args():
    parser = argparse.ArgumentParser(
        description=app_description)

    # args
    parser.add_argument(
        'url', nargs=1, help=url_help)
    parser.add_argument('-M', '--method', choices=["GET", "POST", "PATCH", "PUT",
                                                   "DELETE"], default="GET", help=method_help)
    parser.add_argument('-H', '--header', action='append', help=header_help)
    parser.add_argument('-Q', '--queries', action='append',
                        help=queries_help)
    parser.add_argument('-D', '--data', help=data_help)
    parser.add_argument(
        '--json', help=json_help)
    parser.add_argument('--file', help=file_help)
    parser.add_argument('--timeout', type=float, help=timeout_help)

    args = parser.parse_args()

    return args
