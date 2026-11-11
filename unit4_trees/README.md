## Design Implementation

I started off by programming the Node class, assigning each node with the value, and initializing a left and right node as "None."
Figuring out how recursion worked was a fun puzzle. For both the insert and the search functions I added checks to see if the value is greater than
or less than the value of the node the program is currently at. If it is less than the node, go down the left path through recursion. If it was more than the node,
go down the right.

For inserting a new node once a null/None node is found that is where the value would go. I also added an additional check to see if the value is already in the tree,
and if it was to return a message informing the user. Then I programmed the search function, which was fairly simple. I added a check to see if the current node's value
matched the one that was being search for, and if it was returned True. Otherwise, the program continues down the tree and returns False if it reaches the end of the path.

## Reflection Essay

For this project, I decided to use the BST to sort a list of scheduled employee IDs in the tree. Having never made
a program involving a BST this took some figuring out. It was interesting seeing how the references to a left and right node
worked in python. It was also great practice in seeing how recursion can be used to easily find the next location for a new entry
into the tree.

One of the challenges I faced was that the search function always returned "False" at first, even when I was searching
for an ID I knew for sure was in the tree. It took me a lot longer than I want to admit to realize that the problem was I was
comparing the value that was being searched for to the node itself, instead of the node value. ("if value == node" instead of "if value == node.value")
That section gave me a lot of trouble only because I didn't notice that one little error for so long.

BST structures are an effective way of sorting data as it can effectively cut down the number of nodes a program has to search through, as long as the tree is created evenly.
When searching through a linear, the program has to pass through the entire list if you're searching for a value that isn't in the list.
However, in a BST the program goes down the tree, checking each node to see if the value is greater than or less than the current value.
By sorting data this way you can process a search without passing through every value in the tree.

# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.