"""
    Stack Class

    Attributes:
        - _size: represents how many nodes stored in the stack
        - _top: represents the node that on the top of the stack,
        which will be popped next

    Methods:
        - isEmpty: checks if the stack is empty
        - isFull: checks if the stack is full
        - push: pushes a node into the stack, if the stack is not full
        - pop: pops the node at the top of the stack, if the stack is not empty

    Usage:
        - it stores the custom data named Point
        - you should record your moves in case you must turn back
        - stack structure is proper for this kind of recording (last move should
        be considered first, Last In First Out)
    
"""

from .point import Point

CAPACITY = 50 # capacity of the stack

class Stack:
    def __init__(self):
        self._size = 0
        self._top = None

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == CAPACITY

    def push(self, newNode: Point):
        if not self.isFull():
            newNode.setNext(self._top)
            self._top = newNode
            self._size += 1

    def pop(self):
        if not self.isEmpty():
            removedNode = self._top
            self._top = self._top.getNext()
            self._size -= 1
            return removedNode
