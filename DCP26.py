# Medium

# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

# Should have added that we don't know the length of the singly linked list and cant store the length

from typing import Counter


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class SLL:
    def __init__(self, valueList) -> None:
        self.head = None
        self.tail = None
        for value in valueList:
            self.insert(value)

    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def printList(self):
        currentNode = self.head
        while currentNode != None:
            if currentNode.next == None:
                print(currentNode)
            else:
                print(currentNode, '->', end=' ')
            currentNode = currentNode.next

    def removeFromLast(self, index):  # index will be 1 indexed (starting from 1)
        firstNode = self.head
        secondNode = None
        prevNode = None
        for x in range(index):
            if secondNode == None:
                secondNode = self.head
            else:
                secondNode = secondNode.next
        while secondNode.next != None:
            secondNode = secondNode.next
            firstNode = firstNode.next
            if prevNode == None:
                prevNode = self.head
            else:
                prevNode = prevNode.next
        if prevNode == None:
            self.head = firstNode.next
            firstNode.next = None

        else:
            prevNode.next = firstNode.next
            firstNode.next = None


if __name__ == '__main__':
    ll = SLL([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll.printList()
    ll.removeFromLast(10)
    ll.printList()
