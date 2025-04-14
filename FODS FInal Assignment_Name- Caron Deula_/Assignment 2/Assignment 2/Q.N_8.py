def parse_input_to_int_list(prompt):
    # Helper function to convert comma-separated string input to a list of integers
    user_input = input(prompt)
    try:
        return [int(item.strip()) for item in user_input.split(',')]
    except ValueError:
        print("Please enter valid integers separated by commas.")
        exit(1)

if __name__ == "__main__":
    list1 = parse_input_to_int_list("Enter integers for list 1 (separated by commas): ")
    list2 = parse_input_to_int_list("Enter integers for list 2 (separated by commas): ")

    # (a) Check if lists are of the same length
    if len(list1) == len(list2):
        print("The two lists are of the same length.")
    else:
        print("The two lists are not of the same length.")

    # (b) Check if the sums of the lists are equal
    if sum(list1) == sum(list2):
        print("The sums of both lists are equal.")
    else:
        print("The sums of the lists are not equal.")

    # (c) Check for any common elements between the lists
    common_elements = set(list1) & set(list2)
    if common_elements:
        print("Common values found in both lists:", common_elements)
    else:
        print("There are no common values between the lists.")
