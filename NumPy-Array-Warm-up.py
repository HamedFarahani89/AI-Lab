import numpy as np

length = 8
# Generate a random array
a = np.random.randn(length)

# Uncomment the line below to check if the shape of a is (length,1)
# assert(a.shape == (length,1))

print(a)          # Print the array
print(a.shape)    # Print the shape of the array
print(a.T)        # Print the transpose of the array (since it's a 1D array, it remains the same)
print(np.dot(a,a.T))  # Print the dot product of a with its transpose

# Generate a random array of shape (length,1)
a = np.random.randn(length,1)

# Check if the shape of a is indeed (length,1)
assert(a.shape == (length,1))

print(a)          # Print the array
print(a.shape)    # Print the shape of the array
print(a.T)        # Print the transpose of the array (it will be a row vector)
print(np.dot(a,a.T))  # Print the dot product of a with its transpose
