# Easy

# This problem was asked by Facebook.

# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPriceToCome = []

        for i in reversed(range(len(prices))):
            if len(maxPriceToCome) == 0:
                maxPriceToCome.append(prices[i])
            else:
                maxPriceToCome.append(max(prices[i], maxPriceToCome[-1]))
        maxPriceToCome = list(reversed(maxPriceToCome))
        print(maxPriceToCome)
        maxProfit = 0

        for i in range(len(prices)):
            maxProfit = max(maxProfit, maxPriceToCome[i] - prices[i])

        return maxProfit
