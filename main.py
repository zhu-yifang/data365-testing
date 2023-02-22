import json

with open("response") as f:
    response = json.load(f)
    for post in response["posts"]:
        print(post["post_url"])
        for secondary_link in post["secondary_links"]:
            print(secondary_link["link"])
        print('-' * 80)