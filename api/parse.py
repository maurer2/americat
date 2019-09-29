"""
parse markup for statistics
"""
import os
import sys
import json

from bs4 import BeautifulSoup


def get_file_contents() -> str:
    """Read file content as string"""
    path = os.path.join(sys.path[0], "dump.txt")
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


def map_entry(entry: object) -> dict:
    """Map all entries"""

    child_elements = entry.findChildren(text=True)

    mapped_entry = {
        "state": child_elements[0],
        "householdsOwningACat": child_elements[2],
        "catPopulation": child_elements[4],
        "catsPerHousehold": child_elements[6],
    }

    return mapped_entry


def map_entries(entries: object) -> list:
    """Extract attributes and create new entry from extracted attributes"""

    mapped_entries = list(map(map_entry, entries))

    return mapped_entries


def convert_results_to_list(results: object) -> list:
    """Convert resultsList-type to list"""
    entries_list = list(map(lambda entry: entry.prettify(), results))

    return entries_list


def json_stringify(entries: list) -> str:
    """Create json from list"""
    json_string = json.dumps(entries, indent=4)

    return json_string


def write_file(text: str) -> None:
    """Write to file"""
    path = os.path.join(sys.path[0], "data.json")
    file = open(path, "w")
    file.write(text)
    file.close()


CONTENT = get_file_contents()
ENTRIES = get_entries(CONTENT)
ENTRIES_MAPPED = map_entries(ENTRIES)
JSON_STRING = json_stringify(ENTRIES_MAPPED)

write_file(JSON_STRING)
