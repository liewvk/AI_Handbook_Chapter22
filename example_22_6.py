import json
from urllib.request import Request, urlopen
import chromadb
 
EMBED_MODEL = "nomic-embed-text"
EMBED_API = "http://localhost:11434/api/embed"
records = [
    ("registration", "Registration opens at 8:30 AM.", "schedule.txt"),
    ("equipment", "Bring a Windows laptop and power adapter.",
     "requirements.txt"),
    ("finish", "The workshop ends at 12:00 noon.", "schedule.txt"),
]
 
def embed_many(texts):
    body = json.dumps({"model": EMBED_MODEL,
                       "input": texts}).encode("utf-8")
    request = Request(EMBED_API, data=body,
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=180) as response:
        return json.load(response)["embeddings"]
 
client = chromadb.PersistentClient(path="workshop_vectors")
store = client.get_or_create_collection(
    name="workshop_notes", embedding_function=None)
 
ids = [r[0] for r in records]
texts = [r[1] for r in records]
metadata = [{"source": r[2]} for r in records]
try:
    store.upsert(ids=ids, documents=texts,
                 metadatas=metadata, embeddings=embed_many(texts))
    question = "What time can I register?"
    matches = store.query(
        query_embeddings=embed_many([question]), n_results=2,
        include=["documents", "metadatas", "distances"])
    for text, meta, distance in zip(
            matches["documents"][0], matches["metadatas"][0],
            matches["distances"][0]):
        print(meta["source"], '|', round(distance, 4), '|', text)
except Exception as error:
    print("Check local Ollama and your embedding model:", error)

