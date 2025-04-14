def count_a_in_names(names):
    # Count occurrences of letter 'a' or 'A' in all names combined
    count = 0
    for name in names:
        count += name.lower().count('a')
    return count

if __name__ == "__main__":
    names_input = input("Enter names separated by commas: ")
    # Create a list by stripping any extra whitespace
    names_list = [name.strip() for name in names_input.split(',')]
    a_count = count_a_in_names(names_list)
    print("The letter 'a' appears", a_count, "times in the list.")
