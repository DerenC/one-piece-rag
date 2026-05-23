from rank_bm25 import BM25Okapi
import numpy as np

from corpus_pickle import create_pkl_if_not_exist, get_corpus_docs

def rank_n_filter(query, documents, k=20):
    corpus = [doc.split() for doc in documents]
    bm25 = BM25Okapi(corpus)

    query_arr = query.split()
    scores = bm25.get_scores(query_arr)
    top_k_idx = np.argpartition(scores, -k)[-k:]
    return [documents[i] for i in top_k_idx[np.argsort(-scores[top_k_idx])]]


def retrieve(query, k=50):
    create_pkl_if_not_exist()
    documents = get_corpus_docs()
    return rank_n_filter(query, documents, k)

