# Easy

# This problem was asked by Amazon.

# Implement a stack that has the following methods:

#     push(val), which pushes an element onto the stack
#     pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
#     max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

# Each method should run in constant time.

class Node:
    def __init__(self,value) -> None:
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedList:
    def __init__(self,headNode) -> None:
        self.head = headNode
        self.tail = headNode

    def push(self,val):
        if self.tail:
            self.tail.next = Node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        else:
            self.head = Node(val)
            self.tail = Node(val)

    def pop(self):
        if not self.tail:
            return None
        else:
            result = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return result

    def peek(self):
            return self.tail



class Stack(DoublyLinkedList):
    def __init__(self, headNode) -> None:
        super().__init__(headNode)
        self.maxList = DoublyLinkedList()
    def push(self, val):
        peekValue = self.maxList.peek().val
        if peekValue:            
            if peekValue >= val:
                self.maxList.push(peekValue)
            else:
                self.maxList.push(val)
        else:
            self.maxList.push(val)
        return super().push(val)

    def pop(self):
        self.maxList.pop()
        return super().pop()
    def max(self):
        return self.maxList.peek()
