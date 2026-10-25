"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Create a list for the stack
        self.items = []

    def push(self, value):
        # Add the item to the top of the stack
        self.items.append(value)

    def pop(self):
        # Check if the stack is empty. If it is return an error message
        # Otherwise, remove and return the top item on the stack
        if self.is_empty():
            return "Unable to pop from empty stack."
        return self.items.pop()

    def peek(self):
        # Check if the stack is empty. If it is return an error message
        # Otherwise, return the top value of the stack without removing it
        if self.is_empty():
            return "Unable to peek at an empty stack."
        return self.items[len(self.items) - 1]

    def is_empty(self):
        # Check if the stack is empty and return TRUE if it is.
        return self.items == []


class Queue:
    def __init__(self):
        # Use a deque to create the queue
        self.items = deque()

    def enqueue(self, value):
        # Add the item to the end of the queue
        self.items.append(value)

    def dequeue(self):
        # Check if the stack is empty. If it is return an error message
        # Otherwise, remove and return the first item in the queue
        if self.is_empty():
            return "Unable to dequeue from an empty queue."
        return self.items.popleft()

    def front(self):
        # Check if the stack is empty. If it is return an error message
        # Otherwise, return teh first item in the queue without removing
        if self.is_empty():
            return "Unable to look at the front of an empty queue."
        return self.items[0]

    def is_empty(self):
        # Return TRUE if the length of the queue is zero
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    print("\n=== STACK DEMO ===")

    # Create a stack for a series of operations
    operations = Stack()
    print("Creating a stack with four operations: Paste, Cut, Paste, and Delete")
    # Add four items to the stack
    operations.push("Paste")
    operations.push("Cut")
    operations.push("Paste")
    operations.push("Delete")

    # Display the current top item of the stack
    print("Current item on top:", operations.peek())
    # Remove two items and display what is being removed
    print("Removing two items.")
    print("Popping:", operations.pop())
    print("Popping:", operations.pop())
    # Display the new current top item of the stack
    print("New item on top:", operations.peek())

    # Empty stack to test the error messages for peeking and popping
    print("\nCreating an empty stack and attempting to peek and pop from it.")
    empty_stack = Stack()
    print("Peeking:", empty_stack.peek())
    print("Popping:", empty_stack.pop())

    # Creating a third stack to test the is_empty() call
    print("\nCreating a third stack with only one operation, Delete")
    operations2 = Stack()
    operations2.push("Delete")
    print("Is the stack empty?", operations2.is_empty())
    print("Popping:", operations2.pop())
    print("Is the stack empty?", operations2.is_empty())


    print("\n=== QUEUE DEMO ===")

    # Create a queue for a list of customers
    customers = Queue()
    print("Enqueuing customers: Alice, Bob, Carol, & Dave")
    # Add four customers to the queue
    customers.enqueue("Alice")
    customers.enqueue("Bob")
    customers.enqueue("Carol")
    customers.enqueue("Dave")

    # Display the current front of the queue
    print("Current front of queue:", customers.front())
    # Remove two customers and return the customer that is removed
    print("Dequeuing two customers.")
    print("Dequeuing", customers.dequeue())
    print("Dequeuing", customers.dequeue())
    # Display the new front of the queue
    print("New front of queue:", customers.front())

    # Empty queue to test the error messages
    print("\nCreating an empty queue, and attempting to dequeue from it.")
    empty_queue = Queue()
    print("Dequeuing empty queue:", empty_queue.dequeue())
    print("Front of empty queue:", empty_queue.front())

    # Third queue to test the is_empty() call
    print("\nCreating a third queue with only one customer, Eve.")
    customers2 = Queue()
    customers2.enqueue("Eve")
    print("Is the queue empty?", customers2.is_empty())
    print("Dequeuing", customers2.dequeue())
    print("Is the queue empty?", customers2.is_empty())

if __name__ == "__main__":
    main()
