from embedder import get_embedding
from vector_store import VectorStore
from data_loader import load_documents
from chunker import chunk_text

def build_store_from_file(file_path):
    text = load_documents(file_path)
    chunks = chunk_text(text)

    embeddings = [get_embedding(chunk) for chunk in chunks]
    dim = len(embeddings[0])

    store = VectorStore(dim)
    store.add(embeddings, chunks)

    return store

def retrieve(query, store):
    query_embedding = get_embedding(query)
    return store.search(query_embedding)