import chromadb

client = chromadb.PersistentClient(path="./my_chromadb_data")
collection = client.get_or_create_collection("dialogue")
