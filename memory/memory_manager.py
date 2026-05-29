from memory.vector_store import (
    save_memory,
    search_memory
)

# ==========================
# SAVE POST TO MEMORY
# ==========================

def save_post_memory(post_text):

    save_memory(post_text)

# ==========================
# RETRIEVE RELEVANT MEMORIES
# ==========================

def retrieve_relevant_memories(
    current_post,
    k=3
):

    if not current_post.strip():
        return []

    memories = search_memory(
        current_post,
        k=k
    )

    return memories
# ==========================
# BUILD MEMORY CONTEXT
# ==========================

def build_memory_context(
    current_post
):

    memories = retrieve_relevant_memories(
        current_post
    )

    if not memories:

        return "No previous memories found."

    context = (
        "Relevant Previous Posts:\n\n"
    )

    for index, memory in enumerate(
        memories,
        start=1
    ):

        context += (
            f"{index}. {memory}\n\n"
        )

    return context