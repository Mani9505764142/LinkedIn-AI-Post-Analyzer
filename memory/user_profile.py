import json


def load_user_profile():

    with open(
        "data/user_profile.json",
        "r"
    ) as file:

        return json.load(file)