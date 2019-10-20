"""
dump website body content to file
"""

import os
import sys

from requests_html import HTMLSession

# pylint: disable=line-too-long
URL = "http://www.247wallst.com/special-report/2017/07/19/states-with-the-most-and-least-cat-owners/amp/"


def get_markup(link: str) -> str:
    """Fetch markup"""
    session = HTMLSession()
    url_response = session.get(link)

    return url_response.text


def write_file(text: str) -> None:
    """Write to file"""
    path = os.path.join(sys.path[0], "results/dump.txt")
    file = open(path, "w+")
    file.write(text)
    file.close()


MARKUP = get_markup(URL)

write_file(MARKUP)
