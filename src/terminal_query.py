from query import rag_query

response, sources = rag_query(input("Ask me any question about the anime One Piece\n"))

print(f"\nResponse:\n{response}\n")

print("\nSources:")
for i, source in enumerate(sources):
    print(f"{'---' if i != 0 else ''}\n{source}")
