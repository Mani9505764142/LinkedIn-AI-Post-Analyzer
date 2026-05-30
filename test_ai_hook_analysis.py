from database.viral_post_loader import load_viral_posts
from intelligence.ai_hook_classifier import classify_hook_ai

posts = load_viral_posts()[:3]

for post in posts:

    print("\n" + "=" * 80)

    print(f"Author: {post['author']}")
    print(f"Hook: {post['hook']}")

    print("\nAI ANALYSIS:\n")

    result = classify_hook_ai(
        post["hook"]
    )

    print(result)