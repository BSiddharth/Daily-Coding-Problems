# Medium

# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


class Node:
    def __init__(self, val='root') -> None:
        self.children = [None for x in range(26)]
        self.isEndOfWord = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def add(self, word):
        currentNode = self.root
        for alphabet in word:
            index = self._charToIndex(alphabet)
            if not currentNode.children[index]:
                currentNode.children[index] = Node()
            currentNode = currentNode.children[index]
        currentNode.isEndOfWord = True

    def addList(self, wordsList):
        for word in wordsList:
            self.add(word)

    def _printTrieHelper(self, currentNode, currentString, currentIndex):
        # if currentNode.val != 'root':
        #     currentString += currentNode.val
        if currentNode != self.root:
            currentString += chr(ord('a')+currentIndex)
        if currentNode.isEndOfWord:
            print(currentString)
            return
        for index in range(len(currentNode.children)):
            if currentNode.children[index]:
                self._printTrieHelper(
                    currentNode.children[index], currentString, index)

    def printTrie(self, string):
        currentString = ''
        currentNode = self.root
        currentIndex = 0
        if string != None:
            currentString = string[0:-1]
            for alphabet in string:
                currentIndex = self._charToIndex(alphabet)
                currentNode = currentNode.children[currentIndex]
        self._printTrieHelper(currentNode, currentString, currentIndex)

    def find(self, string):
        currentIndex = 0
        currentNode = self.root
        while currentIndex != len(string):
            if not currentNode.children[self._charToIndex(string[currentIndex])]:
                print(False)
                return
            else:
                currentNode = currentNode.children[self._charToIndex(
                    string[currentIndex])]
                currentIndex += 1

        print(True)


if __name__ == '__main__':
    trie = Trie()
    trie.addList(['dog', 'deer', 'deal'])
    trie.printTrie('de')
    # trie.find('ataga')
