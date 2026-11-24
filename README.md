# AI Handbook — Chapter 22

Python examples exploring vector search and retrieval-augmented generation (RAG) concepts.

## Examples

Run the numbered scripts individually from the repository root:

| File | Topic |
| --- | --- |
| `example_22_1.py` | Cosine similarity for vectors |
| `example_22_2.py` | Ranking passages by cosine similarity with NumPy |
| `example_22_3.py` | Checking Python, NumPy, and Chroma versions |
| `example_22_4.py` | Creating and querying a persistent Chroma collection with sample embeddings |
| `example_22_5.py` | Generating an embedding through the local Ollama API |
| `example_22_6.py` | Storing and querying workshop notes in Chroma using Ollama embeddings |
| `example_22_7.py` | Formatting retrieved passages as grounded prompt context |
| `example_22_8.py` | Updating and deleting Chroma collection records |
| `example_22_9.py` | Calculating Precision@k and Recall@k |

`AI_Handbook_Chapter22.py` is also present in the repository. The persistent Chroma examples use the `vector_store_demo/` and `workshop_vectors/` directories for local data.

## Requirements

- Python 3
- NumPy for examples 22.2 and 22.3
- ChromaDB for examples 22.3, 22.4, 22.6, and 22.8
- For examples 22.5 and 22.6, a local [Ollama](https://ollama.com/) server with the `nomic-embed-text` model available

Install the Python packages with:

```bash
python -m pip install numpy chromadb
```

For the Ollama-based examples, install and start Ollama, then download the model:

```bash
ollama pull nomic-embed-text
```

The scripts call Ollama at `http://localhost:11434`; ensure the local service is running before executing those examples.

## Run an example

From the repository root, for example:

```bash
python example_22_1.py
```

Run any other example by substituting its filename. Some examples create or update local ChromaDB data in the directories listed above.
