from sentence_transformers import CrossEncoder
import numpy as np

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, candidates, k=10):
    scores = reranker.predict([(query, doc) for doc in candidates])
    top_k = np.argsort(scores)[-k:]
    reranked = [candidates[i] for i in top_k[np.argsort(-scores[top_k])]]
    return reranked