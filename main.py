import json
import csv
from pathlib import Path


def make_csv(file_name):
    json_path = Path('./JSON')

    with open(json_path / file_name, 'r') as f:
        response = json.load(f)
        print(response)
    csv_path = Path('./CSV')
    with open(csv_path / (file_name + '.csv'), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["post_url", "secondary_link"])
        for post in response["posts"]:
            temp = []
            temp.append(post["post_url"])
            for secondary_link in post["secondary_links"]:
                temp.append(secondary_link["link"])
            writer.writerow(temp)


def find_all_json_files():
    # find all files starting with "TOP" or "LATEST"
    file_names = []
    p = Path('./JSON')
    for child in p.iterdir():
        if child.is_file() and child.name.startswith(("TOP", "LATEST")):
            file_names.append(child.name)
    return file_names


if __name__ == "__main__":
    file_names = find_all_json_files()
    for file_name in file_names:
        make_csv(file_name)