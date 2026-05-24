import pickle
import os

PKL_FILE_PATH = "data/corpus.pkl"

def create_pkl_if_not_exist():

    if os.path.exists(PKL_FILE_PATH): return

    corpus_set = set()
    folder = 'data/dialogue'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        with open(file_path, "r") as file:
            file_content = file.read()
            for sentence in file_content.split('\n'):
                corpus_set.add(sentence)

    with open(PKL_FILE_PATH, "wb") as file:
        pickle.dump(corpus_set, file)

def get_corpus_docs():
    with open(PKL_FILE_PATH, "rb") as file:
        corpus_set = pickle.load(file)
    return tuple(corpus_set)
