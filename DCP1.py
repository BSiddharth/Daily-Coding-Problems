# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def sumExists(numberList, targetSum):
    numberSet = set()
    for number in numberList:
        difference = targetSum - number
        if difference in numberSet:
            print(True, number, '+', difference)
            return
        else:
            numberSet.add(number)
    print(False)


if __name__ == '__main__':
    sumExists([10, 15, 3, 7], 17)
