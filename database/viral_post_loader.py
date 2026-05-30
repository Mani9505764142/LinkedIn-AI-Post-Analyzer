import json

def load_viral_posts():
    with open("data/viral_posts.json", "r", encoding="utf-8") as file:
        return json.load(file)