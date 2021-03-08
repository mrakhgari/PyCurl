import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "PyCurl is a simple command-line tool for transferring data with URL developed using Python.")

    ## args
    parser.add_argument('url', nargs=1, help="The URL syntax is protocol-dependent. You'll find a detailed description in RFC 3986.")
    parser.add_argument('-M', '--method', choices=["GET", "POST", "PATCH", "PUT", "DELETE"], default="GET", help="The method that you use for sending data.")
    parser.add_argument('-H', '--header', action='append', help=''' (HTTP) Extra header to use when getting a web page.
              You  may  specify any number of extra headers. Note
              that if you should add a custom header that has the
              same  name  as  one of the internal ones curl would
              use,  your  externally  set  header  will  be  used
              instead  of  the  internal  one. This allows you to
              make even trickier stuff than curl  would  normally
              do.  You  should not replace internally set headers
              without knowing perfectly well what you're doing.''')
    parser.add_argument('-Q', '--queries', action='append')
    parser.add_argument('-d', '--data')
    parser.add_argument('--file')
    parser.add_argument('--timeout', type=int)

    args = parser.parse_args()