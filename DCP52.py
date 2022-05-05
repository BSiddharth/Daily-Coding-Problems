# Hard

# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# put(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

# get(key): gets the value at key. If no such key exists, return null.

# Each operation should run in O(1) time.


class Node:
    def __init__(self, val, before=None, after=None) -> None:
        self.val = val
        self.before = before
        self.after = after

    def __repr__(self) -> str:
        return self.val


class LinkedList:
    def __init__(self, capacity) -> None:
        self.start = None
        self.end = None
        self.len = 0
        self.capacity = capacity

    def put(self, node):
        if self.len == self.capacity:
            if self.len == 1:
                self.start = node
                self.end = node
                return
            self.end = self.end.before
            self.end.after = None

            self.start.before = node
            node.after = self.start
            self.start = node
            return

        if self.start == None:
            self.start = node
            self.end = node
        else:
            self.start.before = node
            node.after = self.start
            self.start = node

        self.len += 1

    def bringToStart(self, node):
        if self.start == node:
            return
        if node.after:
            node.after.before = node.before
        else:
            self.end = self.end.before
        node.before.after = node.after

        node.before = None
        node.after = self.start
        self.start.before = node
        self.start = node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyValueDict = {}
        self.keyNodeDict = {}
        self.linkedList = LinkedList(capacity)

    def get(self, key: int) -> int:
        if key not in self.keyValueDict:
            return -1
        else:
            self.linkedList.bringToStart(self.keyNodeDict[key])
            return self.keyValueDict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.keyValueDict:
            self.keyValueDict[key] = value
            self.linkedList.bringToStart(self.keyNodeDict[key])
        else:
            self.keyNodeDict[key] = Node(key)
            if len(self.keyValueDict) >= self.capacity:
                toRemove = self.linkedList.end.val
                self.keyValueDict.pop(toRemove)
                self.keyNodeDict.pop(toRemove)
            self.keyValueDict[key] = value
            self.linkedList.put(self.keyNodeDict[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print(cache.get(1))
# cache.put(3, 3)
# print(cache.get(2))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(3))
# print(cache.get(4))
