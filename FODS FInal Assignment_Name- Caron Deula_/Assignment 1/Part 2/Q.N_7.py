user_input = input("Enter a string: ")

digit_count = 0
letter_count = 0

# Count digits and letters
for char in user_input:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print(f"Number of digits: {digit_count}")
print(f"Number of letters: {letter_count}")