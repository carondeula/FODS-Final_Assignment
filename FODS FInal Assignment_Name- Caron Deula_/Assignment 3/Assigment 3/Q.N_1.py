def count_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

# Example usage
filename = input("Enter the filename: ")
count_file_contents(filename)
