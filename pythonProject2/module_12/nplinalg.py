# np.linalg
# NumPy also supports a wide array of efficient linear algebraic operators
# through the use of its linalg module

import numpy as np

d = np.array([3.0, 0.0]) # dx = 3.0 meters
F = np.array([4.0, 3.0]) # F = 5N
W = np.dot(F, d) # W = F * dx cos theta = F dot dx
print(f"Work:{W} J (kg*m^2/s^2)\n")

m = np.array([[1,3], [2,3]])
print(m)
# two ways to calculate the determinant

# First way:
if np.linalg.det(m) != 0.0:
    print("\nThe matrix is invertible:")
    determinant = m[0,0]*m[1,1]-m[0,1]*m[1,0]
    m_inverse = 1/determinant * np.array([[m[1,1], -m[0,1]], [-m[1,0], m[0,0]]])
    print(f"{m_inverse}\n")
else:
    print("\nThe matrix is not invertible")

# Second way:
# using this linalg.inv() method could make your computation of determinant much easier
m_inverse = np.linalg.inv(m)
print(m_inverse)