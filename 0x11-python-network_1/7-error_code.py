#!/usr/bin/python3
"""
this script takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body
of the response.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
