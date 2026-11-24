import numpy as np
 
passages = ["Registration opens at 8:30 AM.",
            "Bring a Windows laptop.",
            "The workshop ends at noon."]
vectors = np.array([[1., 0.], [0., 1.], [0.8, 0.2]])
query = np.array([1., 0.])
unit = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
query_unit = query / np.linalg.norm(query)
scores = unit @ query_unit
for index in np.argsort(scores)[::-1]:
    print(f"{scores[index]:.3f}: {passages[index]}")

