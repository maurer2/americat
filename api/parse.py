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

    raw_state_and_rank = child_elements[0]
    raw_households_with_cats = child_elements[2]
    raw_cat_population = child_elements[4]
    raw_cats_per_household = child_elements[6]

    mapped_entry = {
        "rank": get_rank(raw_state_and_rank),
        "state": get_state(raw_state_and_rank),
        "householdsWithCats": get_households_with_cats(raw_households_with_cats),
        "catPopulationAbsolute": get_cat_population_absolute(raw_cat_population),
        "catPopulationRelative": get_cat_population_relative(raw_cat_population),
        "catsPerHouseholdAbsolute": get_cats_per_household_absolute(
            raw_cats_per_household
        ),
        "catsPerHouseholdRelative": get_cats_per_household_relative(
            raw_cats_per_household
        ),
    }

    return mapped_entry


def get_rank(text: str) -> str:
    """Extract rank"""

    extracted_text = text.split(".", 1)

    return extracted_text[0].strip()


def get_state(text: str) -> str:
    """Extract state"""
    extracted_text = text.split(".", 1)

    return extracted_text[1].strip()


def get_households_with_cats(text: str) -> str:
    """Extract households with cats relative"""
    extracted_text = text.replace("%", "").replace("(tied)", "")

    return extracted_text.strip()


def get_cat_population_absolute(text: str) -> str:
    """Extract cat population absolute"""
    extracted_text = text.split("(", 1)

    return extracted_text[0].strip()


def get_cat_population_relative(text: str) -> str:
    """Extract cat population relative"""
    extracted_text = text.split("(", 1)

    return extracted_text[1].replace(")", "").strip()


def get_cats_per_household_absolute(text: str) -> str:
    """Extract cats per household absolute"""
    extracted_text = text.split("(", 1)

    return extracted_text[0].strip()


def get_cats_per_household_relative(text: str) -> str:
    """Extract cats per household absolute"""
    extracted_text = text.split("(", 1)

    return extracted_text[1].replace(")", "").strip()


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

print(JSON_STRING)

write_file(JSON_STRING)
