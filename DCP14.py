# Medium

# This problem was asked by Google.

# The area of a circle is defined as πr ^ 2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

import random


def pie(loopCounter):
    counter = 0

    for i in range(loopCounter):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            counter += 1

    print(round((4*counter)/loopCounter, 3))


if __name__ == '__main__':
    pie(10000000)
