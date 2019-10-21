"""
map extracted data
"""

import os
import sys
import json
import re


def get_file_contents() -> str:
    """Read file content as string"""

    path = os.path.join(sys.path[0], "results/data_raw.json")
    file = open(path, "r")
    text = file.read()
    file.close()

    return text


def get_file_entries(content: str) -> list:
    """Parse json"""

    content_parsed = json.loads(content)

    return content_parsed


def map_entry(entry: list) -> dict:
    """Map entries"""

    raw_state_and_rank = entry[0]
    raw_households_with_cats = entry[2]
    raw_cat_population = entry[4]
    raw_cats_per_household = entry[6]

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


def map_entries(entries: list) -> list:
    """Extract attributes and create new entry from extracted attributes"""

    mapped_entries = list(map(map_entry, entries))

    return mapped_entries


def get_rank(text: str) -> str:
    """Extract overall rank"""

    rank = re.findall(r"[0-9]+", text)

    return rank[0].strip()


def get_state(text: str) -> str:
    """Extract state"""

    state = re.findall(r"[a-zA-Z ]+", text)

    return state[0].strip()


def get_households_with_cats(text: str) -> str:
    """Extract households with cats relative"""

    households_with_cats = re.findall(r"[0-9.]+", text)

    return households_with_cats[0]


def get_cat_population_absolute(text: str) -> str:
    """Extract cat population absolute"""

    households_with_cats_absolute = re.findall(r"[0-9.,]+", text)

    return households_with_cats_absolute[0]


def get_cat_population_relative(text: str) -> str:
    """Extract cat population relative"""

    households_with_cats_relative = re.findall(r"\((.*?)\)+", text)

    return households_with_cats_relative[0]


def get_cats_per_household_absolute(text: str) -> str:
    """Extract cats per household absolute"""

    cats_per_household_absolute = re.findall(r"[0-9.,]+", text)

    return cats_per_household_absolute[0]


def get_cats_per_household_relative(text: str) -> str:
    """Extract cats per household absolute"""

    households_with_cats_relative = re.findall(r"\((.*?)\)+", text)

    return households_with_cats_relative[0]


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

    path = os.path.join(sys.path[0], "results/data.json")
    file = open(path, "w")
    file.write(text)
    file.close()


CONTENT = get_file_contents()
ENTRIES = get_file_entries(CONTENT)
ENTRIES_MAPPED = map_entries(ENTRIES)
JSON_STRING = json_stringify(ENTRIES_MAPPED)

write_file(JSON_STRING)
