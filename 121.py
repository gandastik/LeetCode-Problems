#121. You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

def maxProfit(prices: List[int]) -> int:
    max_price, min_price = 0, float('inf')
    for price in prices:
        min_price = min(price, min_price)
        max_price = max(price - min_price, max_price)
    return max_price

prices = [int(x) for x in input().split()]
print(maxProfit(prices))