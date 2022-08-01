#232. Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

class Queue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.items.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.items.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.items[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.items == []
