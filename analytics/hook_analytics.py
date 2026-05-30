from collections import Counter

from database.viral_post_loader import load_viral_posts
from intelligence.hook_classifier import classify_hook


def analyze_hooks():

    posts = load_viral_posts()

    hook_counts = Counter()

    for post in posts:

        hook_type = classify_hook(post["hook"])

        hook_counts[hook_type] += 1

    total_posts = len(posts)

    return hook_counts, total_posts