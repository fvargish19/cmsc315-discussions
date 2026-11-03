"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    lst.insert(index, value)
    """
    This command inserts the value at the given index
    Performance is the best when the index is at the end of the list and nothing else
    in the list has to shift to account for the new value.
    If you add the item at the start of the list every other item is moved to a new
    position, leading to the slowest performance.
    """


def delete_at(lst, index):
    # Check to make sure the index is valid
    if index < -1 or index >= len(lst):
        # If it isn't valid return an error message and stop the process in a safe way
        # This way the program doesn't crash early on
        print("No value at index", index, ", nothing was deleted.")
        return None
    # If it is a valid index remove the item and return the item removed.
    return lst.pop(index)


def search_value(lst, value):
    """
    This is a linear search because it searches through the entire list
    starting at the first index (0) and going all the way to the end.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    print("\n=== INSERTION TESTS ===")

    # Create a list with default values, and then display the list
    list1 = [20, 30, 50]
    print("Original list:", list1)
    # Add an item at the beginning into index 0, and then display the list
    insert_at(list1, 0, 10)
    print("With new value at the beginning:", list1)
    # Add an item in the middle at index 3, and then display the list
    insert_at(list1, 3, 40)
    print("With new value in the middle:", list1)
    # Add an item at the end using the length of the list, and then display the list
    insert_at(list1, len(list1), 60)
    print("With new value at the end:", list1)


    print("\n=== DELETION TESTS ===")
    # Delete an item from index 0, and then display the list
    print("Deleted item:", delete_at(list1, 0))
    print("With value deleted from beginning:", list1)
    # Delete an item from index 1, and then display the list
    print("Deleted item:", delete_at(list1, 1))
    print("With value deleted from middle:", list1)
    # Delete an item from the end using the length of the list, and then display the list
    print("Deleted item:", delete_at(list1, len(list1) - 1))
    print("With value deleted from end:", list1)


    print("\n=== SEARCH TESTS ===")
    print("searching for 40:")
    # Assign the found index to the variable locIndex
    locIndex = search_value(list1, 40)
    # If it's not -1 display the index that is found. Otherwise say it's not located
    if locIndex != -1:
        print("40 found at index", locIndex)
    else:
        print("40 not found.")
    print("Searching for 10:")
    # Assign the found index to the variable locIndex
    locIndex = search_value(list1, 10)
    # If it's not -1 display the index that is found. Otherwise say it's not located
    if locIndex != -1:
        print("10 found at index", locIndex)
    else:
        print("10 not found.")


    print("\n=== EDGE CASES ===")
    print("Deleting from an empty list:")
    list2 = []
    print("List 2:", list2)
    delete_at(list2, 0)
    print("\nInserting into an empty list:")
    insert_at(list2, 0, 10)
    print("List 2 now:", list2)



if __name__ == "__main__":
    main()