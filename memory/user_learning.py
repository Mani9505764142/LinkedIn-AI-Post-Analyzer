from memory.vector_store import vector_db

def build_writing_profile():

    results = vector_db.get()

    documents = results.get(
        "documents",
        []
    )

    if not documents:

        return {
            "total_posts": 0,
            "average_post_length": 0,
            "favorite_topics": []
        }

    total_posts = len(documents)

    average_post_length = int(
        sum(
            len(doc)
            for doc in documents
        ) / total_posts
    )

    topics = {
        "AI": 0,
        "LangChain": 0,
        "RAG": 0,
        "Vector Databases": 0,
        "AWS": 0
    }

    for doc in documents:

        text = doc.lower()

        if "ai" in text:
            topics["AI"] += 1

        if "langchain" in text:
            topics["LangChain"] += 1

        if "rag" in text:
            topics["RAG"] += 1

        if "vector" in text:
            topics["Vector Databases"] += 1

        if "aws" in text:
            topics["AWS"] += 1

    favorite_topics = sorted(
        topics,
        key=topics.get,
        reverse=True
    )

    return {
        "total_posts": total_posts,
        "average_post_length": average_post_length,
        "favorite_topics": favorite_topics[:3]
    }