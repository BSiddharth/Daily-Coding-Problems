# Medium

# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random


def pick(big_stream):
    random_element = None

    for index, element in enumerate(big_stream):
        if index == 0:
            random_element = element
        elif random.randint(1, index + 1) == 1:
            random_element = element
    return random_element


if __name__ == '__main__':
    print(pick([0, 1, 2, 3, 5, 4, 4, 58, 8, 2, 4, 3, ]))
