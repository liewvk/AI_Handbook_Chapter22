import json
from urllib.request import Request, urlopen
 
MODEL = "nomic-embed-text"
API = "http://localhost:11434/api/embed"
 
def embed(text):
    payload = json.dumps({"model": MODEL, "input": text}).encode()
    request = Request(API, data=payload,
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=120) as response:
        result = json.load(response)
    return result["embeddings"][0]
 
try:
    vector = embed("Registration opens at 8:30 AM.")
    print("Embedding dimensions:", len(vector))
    print("First three values:", [round(x, 4) for x in vector[:3]])
except Exception as error:
    print("Embedding request failed:", error)

