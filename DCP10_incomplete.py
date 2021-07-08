# Medium

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


# https://stackoverflow.com/questions/55642383/calling-a-function-with-delay read this!!
import time
from typing import Counter


def scheduler(f, n):
    # wait for n milliseconds
    time.sleep(n/1000)
    f()


if __name__ == '__main__':
    scheduler(lambda: print('Hello World'), 2000)
