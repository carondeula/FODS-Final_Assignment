def is_armstrong(a):
    num_str = str(a)
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == a

num = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
