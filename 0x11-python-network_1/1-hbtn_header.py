#!/usr/bin/python3
"""disps the val of the X-Request-Id var found in
the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
