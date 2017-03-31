import json

from pathlib import Path

def give_me_coords(name):
    jsonpath = Path("/root/developers.json")
    with jsonpath.open() as fo:
        developer_list = json.load(fo)

        for developer in developer_list:
            if developer.get('Name', "") == name:
                return developer.get('Up', 0), developer.get('Right', 0)

    return None