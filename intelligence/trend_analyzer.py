from collections import Counter

from database.viral_post_loader import load_viral_posts


def analyze_topics():

    posts = load_viral_posts()

    topic_counts = Counter()

    for post in posts:

        topic = post["topic"]

        topic_counts[topic] += 1

    return topic_counts