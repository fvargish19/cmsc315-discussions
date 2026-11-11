"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Use recursion to find the first open position in the BST to assign the new value
        # Smaller values go to the left, and bigger values go to the right
        # This makes it easier to search the tree knowing how it should be formatted
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)
            # If the node is empty we found the ideal spot for the new value
        elif value < node.value:
            node.left = self._insert_recursive(node.left, value)
            # If the value is less than the current node go to the left
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
            # If the value is more than the current node go to the right
        else:
            print("Value", value, "already in tree.")
            # If we reach a spot and the value is the same as the current node
            # Display an error message saying that the value is in the tree


    def search(self, value):
        """
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)
        # BST is more efficient than linear search as it starts in the "middle" of the list
        # And can search a tree without going through every item in it. Linear searches
        # will go through the entire tree every time a search is done for an item that isn't
        # in the list.

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        if node is None:
            return False
            # If we reach the end of the tree w/o finding the value return false
        elif value == node.value:
            return True
            # If we find the value return true
        elif value < node.value:
            return self._search_recursive(node.left, value)
            # If the value we're searching for is less than the current value go to the left node
        elif value > node.value:
            return self._search_recursive(node.right, value)
            # If the value we're searching for is more than the current value go to the right node

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        # Create an empty list of values for the sorted tree
        values = []
        # Recursively search the tree starting at the root to sort the tree
        self._inorder_recursive(self.root, values)
        # Return the sorted tree
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    scheduled_employees = BST()
    pending_employees = [712, 423, 980, 820, 217, 720, 130]
    for employee in pending_employees:
        scheduled_employees.insert(employee)

    print("Scheduled employees:", pending_employees)

    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_employees = scheduled_employees.inorder()
    print("Sorted employees:", sorted_employees)

    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("Is 423 scheduled?", scheduled_employees.search(423))
    print("Is 123 scheduled?", scheduled_employees.search(123))
    print("Is 525 scheduled?", scheduled_employees.search(525))
    print("Is 720 scheduled?", scheduled_employees.search(720))

    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASE ===")
    print("Attempting to schedule employee already in the tree:")
    scheduled_employees.insert(217)



if __name__ == "__main__":
    main()