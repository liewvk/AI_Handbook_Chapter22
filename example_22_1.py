import math
 
def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    if len(a) != len(b) or not a or length_a == 0 or length_b == 0:
        raise ValueError("Vectors must have equal, nonzero dimensions")
    return dot / (length_a * length_b)
 
print(f"Similarity: {cosine([1, 2], [2, 4]):.2f}")

