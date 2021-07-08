# Hard

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longestString(string, k):
    wordsDict = {}
    distinctWords = 0
    currentLongestString = ''
    currentString = []
    endIndex = 0
    startIndex = 0
    while endIndex < len(string):
        # print('end index is', endIndex)
        if string[endIndex] in wordsDict:
            # print('current alphabet is', string[endIndex])
            wordsDict[string[endIndex]] += 1
            # print('word dict is', wordsDict)
            currentString.append(string[endIndex])
            # print('current string is', currentString)
            endIndex += 1
        else:
            distinctWords += 1
            # print('distinct word count:', distinctWords)

            if distinctWords <= k:
                wordsDict[string[endIndex]] = 1
                # print('word dict is', wordsDict)
                currentString.append(string[endIndex])
                # print('current string is', currentString)
                endIndex += 1
            else:

                if len(currentString) > len(currentLongestString):
                    currentLongestString = str(''.join(currentString))
                # print('current longest string is', currentLongestString)

                while distinctWords > k:
                    # print('distinct word count:', distinctWords)
                    wordsDict[string[startIndex]] -= 1
                    # print('word dict is', wordsDict)
                    if wordsDict[string[startIndex]] == 0:
                        distinctWords -= 1
                        wordsDict.pop(string[startIndex])
                    # print('distinct word count:', distinctWords)
                    startIndex += 1
                    currentString.pop(0)
                    # print('start index is', startIndex)
                wordsDict[string[endIndex]] = 1
                # print('word dict is', wordsDict)
                currentString.append(string[endIndex])
                # print('current string is', currentString)
                endIndex += 1

    print(currentLongestString)


if __name__ == '__main__':
    longestString("abcba", 2)
