import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="PyCurl is a simple command-line tool for transferring data with URL developed using Python.")

    # args
    parser.add_argument(
        'url', nargs=1, help="The URL syntax is protocol-dependent. You'll find a detailed description in RFC 3986.")
    parser.add_argument('-M', '--method', choices=["GET", "POST", "PATCH", "PUT",
                                                   "DELETE"], default="GET", help="The method that you use for sending data.")
    parser.add_argument('-H', '--header', action='append')
    parser.add_argument('-Q', '--queries', action='append')
    parser.add_argument('-D', '--data')
    parser.add_argument('--json')
    parser.add_argument('--file')
    parser.add_argument('--timeout', type=float)

    args = parser.parse_args()

    return args
