from database.viral_post_loader import load_viral_posts
from intelligence.hook_classifier import classify_hook

posts = load_viral_posts()

for post in posts:
    hook = post["hook"]

    print("-" * 50)
    print(f"Author: {post['author']}")
    print(f"Hook: {hook}")
    print(f"Stored Type: {post['hook_type']}")
    print(f"Detected Type: {classify_hook(hook)}")