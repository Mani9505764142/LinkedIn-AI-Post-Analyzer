def classify_hook(hook):

    hook_lower = hook.lower()

    # Question Hook
    if "?" in hook:
        return "Question"

    # Mistake Hook
    if any(word in hook_lower for word in [
        "mistake",
        "mistakes",
        "failed",
        "failure"
    ]):
        return "Mistake"

    # Data Hook
    if "%" in hook:
        return "Data"

    if any(word in hook_lower for word in [
        "study",
        "research",
        "survey",
        "statistics",
        "data shows"
    ]):
        return "Data"

    # Contrarian Hook
    # Contrarian Hook
    if any(word in hook_lower for word in [
    "everyone",
    "nobody",
    "actually",
    "truth",
    "most founders",
    "most people",
    "nobody talks"
]):
     return "Contrarian"
    # Default → Story Hook
    return "Story"