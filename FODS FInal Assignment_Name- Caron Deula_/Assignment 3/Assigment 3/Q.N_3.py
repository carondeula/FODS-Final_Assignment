def find_and_replace(filename, word_to_find, replacement_word):
    """
    Find and replace a specific word in a file.

    Args:
        filename (str): The name of The file to modify
        word_to_find (str): The word to search for
        replacement_word (str): The word to replace with

    Returns:
        int: The number of replacements made
    """
    try:
        # Open and read The file content
        with open(filename, 'r') as file:
            content = file.read()

        # Count occurrences before replacement
        occurrences = content.count(word_to_find)

        if occurrences == 0:
            print(f"The word '{word_to_find}' was not found in The file.")
            return 0

        # Replace The word
        modified_content = content.replace(word_to_find, replacement_word)

        # Write The modified content back to The file
        with open(filename, 'w') as file:
            file.write(modified_content)

        print(f"Successfully replaced {occurrences} occurrence(s) of '{word_to_find}' with '{replacement_word}'")
        return occurrences

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except PermissionError:
        print(f"Error: Permission denied. Check if you have proper access rights.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


def main():
    # Get input from user
    filename = input("Enter The filename: ")
    word_to_find = input("Enter The word to find: ")
    replacement_word = input("Enter The replacement word: ")

    # Perform find and replace operation
    find_and_replace(filename, word_to_find, replacement_word)


# Execute The main function when script is run
if __name__ == "__main__":
    main()