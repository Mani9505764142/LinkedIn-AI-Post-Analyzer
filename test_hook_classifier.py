from intelligence.hook_classifier import classify_hook

hooks = [
    "Why do startups fail?",
    "I made 5 mistakes building my startup",
    "83% of founders quit too early",
    "Everyone says networking matters",
    "I wasted 10 years building the wrong career",
    "The biggest failure of my career",
    "Nobody talks about this startup lesson"
]

for hook in hooks:
    print(f"{hook} -> {classify_hook(hook)}")