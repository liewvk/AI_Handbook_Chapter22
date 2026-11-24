results = [
    {"source": "schedule.txt", "text": "Registration opens at 8:30 AM."},
    {"source": "requirements.txt", "text": "Bring a laptop."}
]
context = "\n\n".join(
    f"[Source: {r['source']}]\n{r['text']}" for r in results
)
prompt = (
    "Answer only from the following excerpts. Cite filenames. "
    "If the answer is absent, say so.\n\n"
    + context + "\n\nQuestion: When does registration open?"
)
print(prompt)

