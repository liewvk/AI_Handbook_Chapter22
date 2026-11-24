import chromadb
 
client = chromadb.PersistentClient(path="vector_store_demo")
collection = client.get_collection("workshop_demo",
                                   embedding_function=None)
collection.upsert(
    ids=["registration"],
    documents=["Registration now opens at 9:00 AM."],
    embeddings=[[1.0, 0.0]],
    metadatas=[{"source": "schedule.txt", "version": 2}]
)
print("Records before removal:", collection.count())
collection.delete(ids=["ending"])
print("Records after removal:", collection.count())

