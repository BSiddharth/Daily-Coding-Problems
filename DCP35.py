# Hard

# This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def arrangeRGB(array):
    startB = 0
    startG = 0
    for currentIndex in range(len(array)):
        if array[currentIndex] == 'R':
            array[startB], array[currentIndex] = array[currentIndex], array[startB]
            currentIndex = startB
            startB += 1
            array[startG], array[currentIndex] = array[currentIndex], array[startG]
            startG += 1

        elif array[currentIndex] == 'G':
            array[startB], array[currentIndex] = array[currentIndex], array[startB]
            startB += 1
    print(array)


arrangeRGB(['G', 'B', 'B', 'R', 'R', 'B', 'R', 'G', 'R', 'G'])
arrangeRGB(['G', 'R', 'G', 'B', 'R', 'B', 'R', 'B', 'R', 'R', 'B', 'G', 'G'])
arrangeRGB(['G', 'B', 'R', 'B', 'R', 'G', 'R', 'B', 'R', 'R', 'B', 'G'])
arrangeRGB(['G', 'B', 'G', 'R', 'B', 'R', 'B', 'R', 'G', 'G', 'B', ])
