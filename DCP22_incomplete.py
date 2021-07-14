# Medium

# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words(no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either['bed', 'bath', 'and', 'beyond] or ['bedbath', ' and ', 'beyond'].

# Given the set of words 'bed', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return ['bedbath', 'and', 'beyond'].

def originalSentence(words, string):
    wordsSet = set(words)
    startIndex = 0
    result = []
    while startIndex < len(string):
        currentWord = ''
        currentGoodIndex = 0
        for endIndex in range(startIndex+1, len(string)+1):
            if string[startIndex: endIndex] in wordsSet:
                currentWord = string[startIndex: endIndex]
                currentGoodIndex = endIndex
                break
        result.append(currentWord)
        startIndex = currentGoodIndex
    print(result)


if __name__ == '__main__':
    originalSentence(['bed', 'bath', 'bedbath', 'and',
                      'beyond', ],  "bedbathandbeyond")
#  wont work for 3rd example
