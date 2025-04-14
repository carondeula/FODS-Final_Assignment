import pandas as pd

# Create two Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([1, 2, 3, 4, 5])

# Perform operations
addition = series1 + series2
subtraction = series1 - series2
multiplication = series1 * series2
division = series1 / series2

# Display results
print("Series 1:\n", series1)
print("Series 2:\n", series2)
print("\nAddition:\n", addition)
print("\nSubtraction:\n", subtraction)
print("\nMultiplication:\n", multiplication)
print("\nDivision:\n", division)
