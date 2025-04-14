def sorted_names(names_list):
    # Returns the list of names sorted in alphabetical order
    return sorted(names_list)

names_input = input("Enter names separated by commas: ")
# Create a list of names (remove extra whitespace)
names_list = [name.strip() for name in names_input.split(",")]
sorted_list = sorted_names(names_list)
print("Sorted names:", sorted_list)
