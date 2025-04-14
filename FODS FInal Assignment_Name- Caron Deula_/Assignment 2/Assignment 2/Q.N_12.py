if __name__ == "__main__":
    set1 = {20, 40, 60}
    set2 = {10, 20, 50, 40, 90, 750}

    # (a) Union and its length
    union_set = set1 | set2
    print("Union of set1 and set2:", union_set)
    print("Length of union:", len(union_set))

    # (b) Intersection
    intersection_set = set1 & set2
    print("Intersection of set1 and set2:", intersection_set)

    # (c) Symmetric difference
    sym_diff = set1 ^ set2
    print("Symmetric difference between set1 and set2:", sym_diff)

    # (d) Add 40 to set1 and check if the set changes
    original_set1 = set1.copy()
    set1.add(40)
    if set1 == original_set1:
        print("Adding 40 to set1 did not change the set (40 was already present).")
    else:
        print("set1 changed after adding 40:", set1)

    # (e) Remove value 20 from set2
    set2.discard(20)  # Using discard avoids KeyError if value not present
    print("set2 after removing 20:", set2)
