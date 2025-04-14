def filter_integers(integers):
    # Returns a list of numbers that are between 1 and 100 (inclusive)
    return [num for num in integers if 1 <= num <= 100]

if __name__ == "__main__":
    user_input = input("Enter integers separated by commas: ")
    # Convert input into a list of integers
    try:
        numbers = [int(item.strip()) for item in user_input.split(',')]
    except ValueError:
        print("Please ensure you enter valid integers separated by commas.")
        exit(1)
    filtered_numbers = filter_integers(numbers)
    print("Filtered integers (between 1 and 100):", filtered_numbers)
