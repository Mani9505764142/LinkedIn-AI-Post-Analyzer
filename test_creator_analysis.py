from intelligence.creator_analyzer import analyze_creators

results = analyze_creators()

print("\nCREATOR INTELLIGENCE REPORT\n")

sorted_results = sorted(
    results.items(),
    key=lambda item: item[1],
    reverse=True
)

for rank, (creator, count) in enumerate(
    sorted_results,
    start=1
):
    print(f"{rank}. {creator}: {count} posts")