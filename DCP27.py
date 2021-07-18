# Easy

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced(well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
        self.prev = None

    def __str__(self) -> str:
        return str(self.val)


class DLL:
    def __init__(self, valueList=[]) -> None:
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
            node.prev = self.tail
            self.tail = self.tail.next

    def removeLast(self):
        prevNode = self.tail.prev
        if prevNode == None:
            self.head = None
            self.tail = None
        else:
            self.tail = prevNode
            prevNode.next = None


class Stack:
    def __init__(self) -> None:
        self._internalSinglyLinkedList = DLL()
        self.length = 0

    def insert(self, value):
        self._internalSinglyLinkedList.insert(value)
        self.length += 1

    def pop(self):
        self._internalSinglyLinkedList.removeLast()
        self.length -= 1

    def peek(self):
        return self._internalSinglyLinkedList.tail.val


def checkBrackets(string):
    bracketDict = {'[': ']', '{': '}', '(': ')'}
    stack = Stack()
    for symbol in string:
        if stack.length != 0 and stack.peek() not in bracketDict:
            return False
        if stack.length == 0 or bracketDict[stack.peek()] != symbol:
            stack.insert(symbol)
        elif stack.length != 0 and bracketDict[stack.peek()] == symbol:
            stack.pop()
    if stack.length != 0:
        return False
    return True


if __name__ == '__main__':
    assert checkBrackets("([])[]()") == True
    assert checkBrackets("([)]") == False
    assert checkBrackets("((()") == False
