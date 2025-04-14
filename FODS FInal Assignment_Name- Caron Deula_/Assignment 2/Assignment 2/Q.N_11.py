if __name__ == "__main__":
    # (a) Concatenate the dictionaries
    dic1 = {1: 101, 2: 220}
    dic2 = {3: 300, 4: 400}
    dic3 = {5: 510, 6: 610}
    nums = {**dic1, **dic2, **dic3}
    print("Initial concatenated dictionary (nums):", nums)

    # (b) Add a new key/value pair (7, 70)
    nums[7] = 70
    print("After adding (7, 70):", nums)

    # (c) Update the value of key 3 to 80
    if 3 in nums:
        nums[3] = 80
    print("After updating key 3 to 80:", nums)

    # (d) Remove the third item (by insertion order)
    # In Python 3.7+ dictionaries preserve insertion order.
    key_to_remove = list(nums.keys())[2]  # third item has index 2
    removed_value = nums.pop(key_to_remove)
    print(f"After removing the third item (key {key_to_remove}: {removed_value}):", nums)

    # (e) Sum all the values in nums
    total_sum = sum(nums.values())
    print("Sum of all values in nums:", total_sum)

    # (f) Multiply all the values in nums
    product = 1
    for value in nums.values():
        product *= value
    print("Product of all values in nums:", product)

    # (g) Retrieve the maximum and minimum values in nums
    max_value = max(nums.values())
    min_value = min(nums.values())
    print("Maximum value in nums:", max_value)
    print("Minimum value in nums:", min_value)
