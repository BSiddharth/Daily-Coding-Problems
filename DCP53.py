# Medium

# This problem was asked by Apple.

# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

from collections import deque


class MyQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.activeQ = self.q1
        self.nonActiveQ = self.q2

    def push(self, x: int) -> None:
        self.activeQ.append(x)

    def pop(self) -> int:
        while len(self.activeQ) != 0:
            toAdd = self.activeQ.pop()
            self.nonActiveQ.append(toAdd)
        toReturn = self.nonActiveQ.pop()

        while len(self.nonActiveQ) != 0:
            toAdd = self.nonActiveQ.pop()
            self.activeQ.append(toAdd)

        return toReturn

    def peek(self) -> int:
        if len(self.activeQ) == 0:
            return None
        else:
            while len(self.activeQ) != 0:
                toAdd = self.activeQ.pop()
                self.nonActiveQ.append(toAdd)

            toReturn = self.nonActiveQ[-1]

            while len(self.nonActiveQ) != 0:
                toAdd = self.nonActiveQ.pop()
                self.activeQ.append(toAdd)

            return toReturn

    def empty(self) -> bool:
        return len(self.activeQ) == 0
