from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import os

load_dotenv()

minilm_emb_model = SentenceTransformer('all-MiniLM-L6-v2', token=os.environ.get("HF_TOKEN"))  # 384-dim embeddings

def minilm_encode(texts: list[str]):
    return minilm_emb_model.encode(texts)

# TODO
# mpnet_emb_model = SentenceTransformer('microsoft/mpnet-base', token=os.environ.get("HF_TOKEN"))  # 384-dim embeddings

# def mpnet_encode(texts: list[str]) -> list[list[float]]:
#     return mpnet_emb_model.encode(texts)


encode = minilm_encode
