#!/usr/bin/python3
"""disps the val of the X-Request-Id var found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    html = get(argv[1])
    print(html.headers.get('X-Request-Id'))
