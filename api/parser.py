"""
parse markup for statistics
"""
import os
import sys
import json

from bs4 import BeautifulSoup


def get_file_contents() -> str:
    """Read file content as string"""
    path = os.path.join(sys.path[0], "results/dump.txt")
    file = open(path, "r")
    text = file.read()
    file.close()

    return text


def get_entries(markup: str) -> list:
    """Get array of entries"""
    try:
        parsed_body = BeautifulSoup(markup, "html.parser")
        container = parsed_body.select(".amp-wp-article-content")
        # first amp-wp-inline is empty
        entries = container[0].select(
            "p[class^=amp-wp-inline-] ~ p[class^=amp-wp-inline-]"
        )

        return entries

    except Exception as exception:
        print(exception)
        return []


def extract_entries(entries: object) -> list:
    """Extract attributes and create new entry from extracted attributes"""

    mapped_entries = list(map(extract_entry, entries))

    return mapped_entries


def extract_entry(entry: object) -> dict:
    """Map all entries"""

    child_elements = entry.findChildren(text=True)

    trimmed = list(map(str.strip, child_elements))

    return trimmed


def json_stringify(entries: list) -> str:
    """Create json from list"""
    json_string = json.dumps(entries, indent=4)

    return json_string


def write_file(text: str) -> None:
    """Write to file"""
    path = os.path.join(sys.path[0], "results/data_raw.json")
    file = open(path, "w+")
    file.write(text)
    file.close()


CONTENT = get_file_contents()
ENTRIES = get_entries(CONTENT)
ENTRIES_MAPPED = extract_entries(ENTRIES)
JSON_STRING = json_stringify(ENTRIES_MAPPED)

write_file(JSON_STRING)
