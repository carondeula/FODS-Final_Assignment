def word_count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()

        words = text.split()
        word_dict = {}

        for word in words:
            word = word.strip(",.!?()[]{}\"\'")  # Clean punctuation
            word_dict[word] = word_dict.get(word, 0) + 1

        for word, count in word_dict.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found.")

# Example usage
filename = input("Enter the filename you want: ")
word_count(filename)
