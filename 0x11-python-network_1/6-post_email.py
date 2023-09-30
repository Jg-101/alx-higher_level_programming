#!/usr/bin/python3
"""disps the val of the X-Request-Id var found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)
