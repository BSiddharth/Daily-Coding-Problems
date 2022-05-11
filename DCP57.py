# Medium

# This problem was asked by Amazon.

# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


# *********************************************LEETCODE VERSION*********************************************

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified and no extra space is inserted between words.

# Note:

#   A word is defined as a character sequence consisting of non-space characters only.
#   Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#   The input array words contains at least one word.


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentIndex = 0
        currentWidth = 0
        wordsBuffer = []
        result = []

        while currentIndex < len(words):
            while currentWidth + len(words[currentIndex]) <= maxWidth:
                wordsBuffer.append(words[currentIndex])
                currentWidth += len(words[currentIndex])
                currentIndex += 1

                if currentIndex == len(words):
                    break
                if currentWidth + len(words[currentIndex]) + 1 <= maxWidth:
                    wordsBuffer[-1] = wordsBuffer[-1] + " "
                    currentWidth += 1
                else:
                    break
            spacesToAdd = maxWidth - currentWidth

            if currentIndex < len(words):
                if len(wordsBuffer) == 1:
                    wordsBuffer[0] = wordsBuffer[0] + spacesToAdd * " "
                else:
                    spaceToAddInBetween = spacesToAdd // (len(wordsBuffer) - 1)

                    for i in range(len(wordsBuffer) - 1):
                        wordsBuffer[i] = wordsBuffer[i] + spaceToAddInBetween * " "
                    spaceToAddInBetween = spacesToAdd % (len(wordsBuffer) - 1)
                    i = 0
                    while spaceToAddInBetween != 0:
                        wordsBuffer[i] = wordsBuffer[i] + " "
                        i += 1
                        spaceToAddInBetween -= 1

                toAdd = "".join(wordsBuffer)
                result.append(toAdd)
            else:
                toAdd = "".join(wordsBuffer)
                toAdd += spacesToAdd * " "
                result.append(toAdd)
            currentWidth = 0
            wordsBuffer = []

        return result
