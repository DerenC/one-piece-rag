# One Piece RAG

This is a RAG chatbot where you can ask it any question about the anime, One Piece.

The RAG has indexed many snippets of dialogues (with the character names) from episode 382 to 777. 

[Link to the dataset](https://huggingface.co/datasets/mramazan/One-Piece-Transcripts-with-Character-Names-382-777)

Instructions on setting up the project: 

## 1. Turn raw csv file data to text files

```bash
python3 src/csv2dialogue.py
```

All dialogues from each episode will be saved to a single text file under the directory, "data/dialogue". The same dialogue consecutively from the same character will also be concatenated.

## 2. Chunk, Embed and Index all documents in a ChromaDB

```bash
python3 src/index.py
```

As ChromaDB PersistentClient is used, a directory named "chromadb_data". The whole database will be setup based on the files in this directory.

## 3. Ask any question you like

```bash
python3 src/query.py
```

Key in the question you want to ask into the terminal. And voilà!

## Possible future extensions

- Explore different embedding models under `chromadb.utils.embedding_functions`
