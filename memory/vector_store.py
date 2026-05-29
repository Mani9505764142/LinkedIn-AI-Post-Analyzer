import os

from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
# ==========================
# LOAD ENV VARIABLES
# ==========================

load_dotenv()

# ==========================
# EMBEDDING MODEL
# ==========================

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
# ==========================
# CHROMA DATABASE
# ==========================

vector_db = Chroma(
    persist_directory="memory/chroma_db",
    embedding_function=embeddings
)

# ==========================
# SAVE MEMORY
# ==========================

def save_memory(text):

    vector_db.add_texts(
        texts=[text]
    )

# ==========================
# SEARCH MEMORY
# ==========================

def search_memory(query, k=3):

    if not query.strip():
        return []

    results = vector_db.similarity_search(
        query,
        k=k
    )

    return [
        doc.page_content
        for doc in results
    ]