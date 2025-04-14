import numpy as np

# Create a 5x5 matrix where each row has values from 0 to 4
matrix = np.tile(np.arange(5), (5, 1))
print("5x5 Matrix with row values from 0 to 4:\n", matrix)
