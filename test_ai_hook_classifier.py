from intelligence.ai_hook_classifier import classify_hook_ai

hooks = [
    "The 'Portfolio Career' is replacing the 9-to-5.",
    "The most dangerous trap in your 20s and 30s.",
    "90% of LinkedIn content is painfully boring.",
    "Stop pitching in the first direct message."
]

for hook in hooks:

    print("\n" + "=" * 60)

    print("HOOK:")
    print(hook)

    print("\nAI ANALYSIS:\n")

    result = classify_hook_ai(hook)

    print(result)