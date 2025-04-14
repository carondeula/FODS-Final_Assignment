import numpy as np

'''
Description of program:
This program creates a NumPy array of size 10 containing evenly spaced values
that range from 0 to 1, but explicitly excludes the values 0 and 1 themselves.
It demonstrates how to create arrays with specific value constraints and array slicing.
'''

def create_range_vector():
    """
    Creates a vector of size 10 with values ranging from 0 to 1, both excluded
    
    Returns:
        A numpy array of size 10 with values between 0 and 1 (exclusive)
    """
    # Create a vector with 10 equally spaced values between 0 and 1
    vector = np.linspace(0, 1, 12)[1:-1]
    
    return vector

# Test the function
result = create_range_vector()
print(result)