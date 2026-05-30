from collections import Counter

from database.viral_post_loader import load_viral_posts


def analyze_creators():

    posts = load_viral_posts()

    creator_counts = Counter()

    for post in posts:
        creator_counts[post["author"]] += 1

    return creator_counts