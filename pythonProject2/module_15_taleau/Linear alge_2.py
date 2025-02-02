import numpy as np

# Define the matrix A and vector b
A = np.array([
    [12, 8],
    [8, 10]
], dtype=float)

b = np.array([-24,-2], dtype=float)

# Augment the matrix A with b
augmented_matrix = np.column_stack((A, b))

# Perform Gaussian elimination
n = len(b)

# Forward elimination
for i in range(n):
    # Make the diagonal element 1 by dividing the row
    factor = augmented_matrix[i, i]
    augmented_matrix[i] = augmented_matrix[i] / factor

    # Eliminate the entries below the pivot
    for j in range(i + 1, n):
        factor = augmented_matrix[j, i]
        augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

# Back substitution
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:n], x[i + 1:n])

print("Solution x:", x)