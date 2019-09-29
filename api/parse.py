"""
parse markup for statistics
"""
import os
import sys

from bs4 import BeautifulSoup


def get_file_contents() -> str:
    """Read file content as string"""
    path = os.path.join(sys.path[0], "dump.txt")
    file = open(path, "r")
    text = file.read()
    file.close()

    return text


# def get_entries(markup: str) -> List:
def get_entries(markup: str):
    """Get array of entries"""
    try:
        parsed_body = BeautifulSoup(markup, "html.parser")

        # https://stackoverflow.com/questions/18725760/beautifulsoup-findall-given-multiple-classes
        container = parsed_body.find_all(True, {"class": "amp-wp-article-content"})
        entries = container[0].find_all(True, {"class": "wp-caption"})

        return entries

    except Exception as exception:
        print(exception)
        return []


CONTENT = get_file_contents()
ENTRIES = get_entries(CONTENT)

print(len(ENTRIES))
