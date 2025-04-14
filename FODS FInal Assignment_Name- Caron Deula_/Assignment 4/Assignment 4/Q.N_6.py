import numpy as np

'''
Description of program:
This program takes user input to create an array of at least 10 numbers.
It then sorts the array and performs various slicing operations to extract
elements from specific index ranges (2-5, 5-8, and 2-9).
The program demonstrates array input, sorting, and slicing operations in NumPy.
'''

def array_operations():
    """
    Takes user input for an array, sorts it, and performs slicing operations
    
    Returns:
        The original array, sorted array, and various slices
    """
    # Get user input for array elements
    input_str = input("Enter at least 10 numbers separated by spaces: ")
    
    # Convert input string to a list of numbers
    input_list = [float(x) for x in input_str.split()]
    
    # Check if at least 10 elements were provided
    if len(input_list) < 10:
        print("Error: Please enter at least 10 numbers")
        return None
    
    # Convert to numpy array and sort
    array = np.array(input_list)
    sorted_array = np.sort(array)
    
    # Perform slicing operations
    slice_2_5 = sorted_array[2:6]  # Elements from index 2 to 5 (inclusive)
    slice_5_8 = sorted_array[5:9]  # Elements from index 5 to 8 (inclusive)
    slice_2_9 = sorted_array[2:10]  # Elements from index 2 to 9 (inclusive)
    
    return array, sorted_array, slice_2_5, slice_5_8, slice_2_9

# Test the function
result = array_operations()
if result:
    original, sorted_arr, slice1, slice2, slice3 = result
    print("Original array:", original)
    print("Sorted array:", sorted_arr)
    print("Elements between indexes 2-5:", slice1)
    print("Elements between indexes 5-8:", slice2)
    print("Elements between indexes 2-9:", slice3)