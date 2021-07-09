# Easy

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

#     record(order_id): adds the order_id to the log
#     get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.


# We can use a list to optimize read and a double linked list to optimize insertions and deletions


class LimitedStack:
    def __init__(self, n) -> None:
        self.len = 0
        self.internalList = []
        self.lenLimit = n

    def record(self, order_id):
        if self.lenLimit == 0:
            print('Adding not possible')
        elif self.len == self.lenLimit:
            self.internalList.pop(0)
            self.internalList.append(order_id)
        else:
            self.internalList.append(order_id)
            self.len += 1

    def get_last(self, i):
        if i <= self.len:
            print(self.internalList[-i])
        else:
            print('Not enough logs')


if __name__ == '__main__':
    ls = LimitedStack(4)
    ls.record(1)
    ls.record(2)
    ls.record(3)
    ls.get_last(2)
    ls.get_last(3)
    ls.get_last(1)
    ls.record(4)
    ls.get_last(2)
    ls.get_last(3)
    ls.get_last(1)
    ls.record(5)
    ls.get_last(2)
    ls.get_last(3)
    ls.get_last(1)
