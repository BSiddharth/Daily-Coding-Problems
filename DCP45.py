# Easy

# This problem was asked by Two Sigma.

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand10() that returns an integer from 1 to 10 (inclusive).


class Solution:
    def rand10(self):
        a = rand7()
        b = rand7()
        random10 = ((a - 1) * 7) + (b - 1)

        if random10 >= 40:
            return self.rand10()
        else:
            return (random10 % 10) + 1
