import csv
import json
from typing import List, Dict, Union


def csv_to_dict(csv_file: str) -> List[Dict[str, Union[str, int]]]:
    """
    The csv_to_dict function takes as an argument the name and location of a file with data in CSV format
    as a string. When called, it opens a file for reading, reads data and converts it into a dictionary
    in python format. Returns the resulting dictionary in python format.
    """
    with open(csv_file, 'r', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        json_arr: list = []
        for row in csv_reader:
            json_arr.append(row)

    return json_arr


def write_json(json_list: list) -> None:
    """
    The write_json function takes as an argument a dictionary in the format necessary to form the initial values
    of the database in the form of a dictionary. When called, it converts the dictionary to JSON format,
    opens a file for writing and writes data to a file in JSON format.
    """
    json_str: str = json.dumps(json_list, ensure_ascii=False)
    with open('data.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json_str)


json_list: list = []
list_ads: list = csv_to_dict('location.csv')
for row in list_ads:
    json_list.append({
        "model": "author.location",
        "pk": int(row["id"]),
        "fields": {
            "name": row["name"],
            "lat": float(row["lat"]),
            "lng": float(row["lng"])
        }})

list_category: list = csv_to_dict('user.csv')
for row in list_category:
    json_list.append({
        "model": "author.user",
        "pk": int(row["id"]),
        "fields": {
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "username": row["username"],
            "password": row["password"],
            "role": row["role"],
            "age": int(row["age"]),
            "location_id": int(row["location_id"])
        }})

write_json(json_list)
