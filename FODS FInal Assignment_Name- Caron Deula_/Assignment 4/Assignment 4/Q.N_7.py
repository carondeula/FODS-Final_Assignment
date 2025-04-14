import numpy as np

'''
Description of program:
This program creates a random array of 10 integers, sorts it, and then
reshapes it into two different matrix dimensions: 2x5 and 5x2.
The program demonstrates random array generation, sorting, and reshaping operations in NumPy.
It shows how the same data can be restructured into matrices with different dimensions
while preserving the data values and their order.
'''

def reshape_array():
    """
    Creates an array of random integers, sorts it, and reshapes it into different dimensions
    
    Returns:
        The original array, sorted array, and reshaped arrays
    """
    # Create a random array of integers (1x10)
    random_array = np.random.randint(1, 100, 10)
    
    # Sort the array
    sorted_array = np.sort(random_array)
    
    # Reshape into 2x5 matrix
    reshaped_2x5 = sorted_array.reshape(2, 5)
    
    # Reshape into 5x2 matrix
    reshaped_5x2 = sorted_array.reshape(5, 2)
    
    return random_array, sorted_array, reshaped_2x5, reshaped_5x2

# Test the function
original, sorted_arr, reshape1, reshape2 = reshape_array()
print("Original array:", original)
print("Sorted array:", sorted_arr)
print("\nReshaped into 2x5 matrix:")
print(reshape1)
print("\nReshaped into 5x2 matrix:")
print(reshape2)