#!/usr/bin/python3
# Python script that takes in a URL sends a request to the URL
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
