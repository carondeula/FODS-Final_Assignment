import numpy as np

# Ask user for input
a = int(input("Enter number of rows (a): "))
b = int(input("Enter number of columns (b): "))

# Generate random array
random_array = np.random.rand(a, b)

# Calculate average
average = np.mean(random_array)

# Print the array and average
print("\nGenerated Array:\n", random_array)
print("Average of array values:", average)
