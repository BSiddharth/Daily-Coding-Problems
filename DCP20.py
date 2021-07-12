# Easy

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time(where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    def __init__(self, internalList=[]) -> None:
        self.head = None
        self.tail = None
        self.len = 0
        for val in internalList:
            self.insert(val)

    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.len += 1

    def printList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode)
            currentNode = currentNode.next


def findIntersection(ll1, ll2):
    len1 = ll1.len
    len2 = ll2.len
    diff = abs(len1-len2)
    firstNode = ll1.head if len1 > len2 else ll2.head
    secondNode = ll1.head if len1 <= len2 else ll2.head
    for x in range(diff):
        firstNode = firstNode.next
    for x in range(min(len1, len2)):
        if firstNode != None and firstNode.val == secondNode.val:
            print('common node is', firstNode.val)
            return
        firstNode = firstNode.next
        secondNode = secondNode.next

    print('no common node')


if __name__ == '__main__':
    findIntersection(LinkedList([1, 2, 3, 4, 5, 6]),
                     LinkedList([1, 0, 2, 2, 2, 9, 8, 7, 4, 5, 6]))
    # LinkedList([10, 9, 8, 7, 4, 5, 6]).printList()
