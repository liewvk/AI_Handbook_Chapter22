relevant = {"registration", "schedule"}
retrieved = ["registration", "equipment", "finish"]
k = 3
hits = len(relevant.intersection(retrieved[:k]))
precision_at_k = hits / k
recall_at_k = hits / len(relevant)
print(f"Precision@{k}: {precision_at_k:.2f}")
print(f"Recall@{k}: {recall_at_k:.2f}")

