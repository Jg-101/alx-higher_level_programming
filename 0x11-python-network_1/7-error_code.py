#!/usr/bin/python3
"""disps the val of the X-Request-Id var found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
