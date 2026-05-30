from intelligence.trend_analyzer import analyze_topics

results = analyze_topics()

print("\nTREND INTELLIGENCE REPORT\n")

sorted_results = sorted(
    results.items(),
    key=lambda item: item[1],
    reverse=True
)

for rank, (topic, count) in enumerate(
    sorted_results,
    start=1
):

    print(f"{rank}. {topic}: {count} posts")