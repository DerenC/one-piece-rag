from sentence_transformers import SentenceTransformer

emb_model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim embeddings

def encode(texts: list[str]):
    return emb_model.encode(texts)
