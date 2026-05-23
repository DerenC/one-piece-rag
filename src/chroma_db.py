import chromadb

import emb_model

client = chromadb.PersistentClient(path="./chromadb_data")
collection = client.get_or_create_collection("dialogue")

def retrieve(query, k=100):
    query_embedding = emb_model.encode([query])
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=k
    )
    if results is None or results.get("documents") is None: return ["No relevant reference is found"]

    return [doc for sublist in results.get("documents") for doc in sublist] # type: ignore
