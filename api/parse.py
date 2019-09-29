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


def get_entries(markup: str):
    # def get_entries(markup: str) -> List:
    """Get array of entries"""
    try:
        parsed_body = BeautifulSoup(markup, "html.parser")
        container = parsed_body.select(".amp-wp-article-content")
        # first amp-wp-inline is empty
        entries = container[0].select("p[class^=amp-wp-inline-] ~ p[class^=amp-wp-inline-]")

        return entries

    except Exception as exception:
        print(exception)
        return []


def map_entry(entry):
    """Map all entries"""

    child_elements = entry.findChildren(text=True)

    mapped_entry = {
        "state": child_elements[0],
        "householdsOwningACat": child_elements[2],
        "catPopulation": child_elements[4],
        "catsPerHousehold": child_elements[6],
    }

    return mapped_entry


def map_entries(entries):
    """Extract attributes and create new entry from extracted attributes"""

    mapped_entries = list(map(map_entry, entries))

    return mapped_entries


def convert_results_to_list(results):
    """Convert resultsList-type to list"""
    entries_list = list(map(lambda entry: entry.prettify(), results))

    return entries_list


CONTENT = get_file_contents()
ENTRIES = get_entries(CONTENT)
ENTRIES_MAPPED = map_entries(ENTRIES)

print(ENTRIES_MAPPED)
