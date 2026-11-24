import chromadb
 
client = chromadb.PersistentClient(path="vector_store_demo")
collection = client.get_or_create_collection(
    name="workshop_demo",
    metadata={"hnsw:space": "cosine"},
    embedding_function=None
)
collection.upsert(
    ids=["registration", "laptop", "ending"],
    documents=["Registration opens at 8:30 AM.",
               "Bring a Windows laptop.",
               "The workshop ends at noon."],
    embeddings=[[1.0, 0.0], [0.0, 1.0], [0.8, 0.2]],
    metadatas=[{"source": "schedule.txt"},
               {"source": "requirements.txt"},
               {"source": "schedule.txt"}]
)
result = collection.query(
    query_embeddings=[[1.0, 0.0]],
    n_results=2,
    include=["documents", "metadatas", "distances"]
)
for doc, meta, dist in zip(result["documents"][0],
                           result["metadatas"][0],
                           result["distances"][0]):
    print(f"{dist:.3f} | {meta['source']} | {doc}")

