from analytics.hook_analytics import analyze_hooks

results, total_posts = analyze_hooks()

print("\nHOOK ANALYTICS REPORT\n")

sorted_results = sorted(
    results.items(),
    key=lambda item: item[1],
    reverse=True
)

for rank, (hook_type, count) in enumerate(
    sorted_results,
    start=1
):

    percentage = (count / total_posts) * 100

    print(
        f"{rank}. {hook_type}: "
        f"{count} posts "
        f"({percentage:.1f}%)"
    )