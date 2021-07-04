# Hard
# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# With division it is easy. Just store the product of whole list and replace each element with product/element

def withoutDiv(numbersList):
    # It stores the product of all the numbers that are left to current number
    leftProduct = [1 for x in range(len(numbersList))]
    # It stores the product of all the numbers that are right to current number
    rightProduct = [1 for x in range(len(numbersList))]

    for index in range(len(numbersList)):
        if 0 < index:
            leftProduct[index] = leftProduct[index-1]*numbersList[index-1]
            rightProduct[len(numbersList)-1-index] = rightProduct[len(
                numbersList)-index]*numbersList[len(numbersList)-index]

    for index in range(len(numbersList)):
        numbersList[index] = leftProduct[index]*rightProduct[index]
    print(numbersList)


if __name__ == '__main__':
    withoutDiv([1, 2, 3, 4, 5])
    withoutDiv([3, 2, 1])
