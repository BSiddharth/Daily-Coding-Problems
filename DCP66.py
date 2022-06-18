# Medium

# This problem was asked by Square.

# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

# Write a function to simulate an unbiased coin toss.

from random import randint


def biased():
    l = [0, 1, 1]
    i = randint(0, 2)
    return l[i]


def unbiased():
    x = biased()
    y = biased()

    while x != y:
        x = biased()
        y = biased()

    return x
