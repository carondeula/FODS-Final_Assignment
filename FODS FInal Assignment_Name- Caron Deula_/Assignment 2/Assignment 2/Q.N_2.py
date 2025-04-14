
def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    # Check for factors from 2 to sqrt(n)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number to check if it is prime: "))
if is_prime(number):
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")