# Medium
# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    pairSet = pair(lambda x, y: [x, y])
    print(pairSet[0])
    return


def cdr(pair):
    pairSet = pair(lambda x, y: [x, y])
    print(pairSet[1])
    return


if __name__ == '__main__':
    car(cons(3, 4))
    cdr(cons(3, 4))
