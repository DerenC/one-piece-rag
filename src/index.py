from langchain_text_splitters import RecursiveCharacterTextSplitter
import emb_model
from chroma_db import collection
import os

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " "]  # Try these in order
)

folder = 'data/dialogue'
start_idx = 0
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    episode = int(filename.replace(".txt", ""))
    with open(file_path, "r") as file:
        chunks = splitter.split_text(file.read())
        num_of_chunks = len(chunks)
        end_idx = start_idx + num_of_chunks
        embeddings = emb_model.encode(chunks)
        collection.upsert(
            documents=chunks,
            embeddings=embeddings.tolist(),
            ids=list(map(str, range(start_idx, end_idx))),
            metadatas = [{"episode": episode} for _ in range(num_of_chunks)]
        )

        start_idx = end_idx
