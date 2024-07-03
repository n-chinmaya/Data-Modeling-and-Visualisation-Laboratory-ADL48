import numpy as np

# Create a 2D array
array = np.array([[4, 2, 7],
                  [1, 5, 3],
                  [8, 6, 9]])
reversed_array = array[::-1, ::-1]
principal_diagonal = np.diag(array)
sorted_array_ascending = np.sort(array, axis=1)
sorted_array_descending = np.sort(array, axis=1)[:, ::-1]
print("Original 2D Array:\n",array)
print("\nArray Elements in Reverse Order:\n", reversed_array)
print("\nPrincipal Diagonal Elements:\n",principal_diagonal)
print("\n2D Array Rows Sorted in Ascending Order:\n",sorted_array_ascending)
print("\n2D Array Rows Sorted in Descending Order:\n",sorted_array_descending)
