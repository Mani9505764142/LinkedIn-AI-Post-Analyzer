from database.viral_post_loader import load_viral_posts

posts = load_viral_posts()

print(f"Total Posts: {len(posts)}")
print(posts[0]["author"])
print(posts[0]["hook"])