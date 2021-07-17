# Medium

# This problem was asked by Google.

# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

#     is_locked, which returns whether the node is locked
#     lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
#     unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

# You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.


class Btree:
    def __init__(self, length=0) -> None:
        self.root = None
        self._internalValueList = [x for x in range(length)]
        self._internalLockList = [False for x in range(length)]

    def checkAncestors(self, index) -> bool:
        if index < 0:
            print(True)
            return True
        if self._internalLockList[index]:
            print(False)
            return False
        return self.checkAncestors(int((index+1)/2)-1 if index % 2 == 0 else int(index/2)-1)

    def checkDescendants(self, index) -> bool:
        if index >= len(self._internalValueList):
            print(True)
            return True
        if self._internalLockList[index]:
            print(False)
            return False
        return self.checkDescendants(2*index+1) and self.checkDescendants(2*index+2)

    def lock(self, index) -> bool:
        if self.checkAncestors(index) and self.checkDescendants(index):
            self._internalLockList[index] = True
            print(True)
            return True
        else:
            print(False)
            return False


if __name__ == '__main__':
    bTree = Btree(15)
    assert bTree.lock(4) == True
    assert bTree.lock(13) == True
    assert bTree.lock(2) == False
    assert bTree.lock(1) == False
    assert bTree.lock(7) == True
    assert bTree.lock(0) == False
