def count_case(input_string):
    # Initialize counters for uppercase and lowercase letters.
    upper_count = 0
    lower_count = 0

    # Loop through each character in the string.
    for char in input_string:
        if char.isupper():
            upper_count += 1  # Count uppercase letters.
        elif char.islower():
            lower_count += 1  # Count lowercase letters.

    # Return the counts as a tuple.
    return upper_count, lower_count


# Example usage:
Result = input("Enter a string: ")
upper, lower = count_case(Result)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
