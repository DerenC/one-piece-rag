from sentence_transformers import CrossEncoder
import numpy as np

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query, candidates, k=5):
    scores = reranker.predict([(query, doc) for doc in candidates])
    reranked = [candidates[i] for i in np.argsort(scores)[-k:]]
    return reranked