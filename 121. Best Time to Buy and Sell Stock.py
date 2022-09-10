# ugly-ass solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prune tail of falling elements
        try:
            while prices[-2] >= prices[-1]:
                prices.pop(-1) # instead, find the last growing index and  slice list
        except IndexError:
            return 0

        min_val = prices[0]
        max_d = max(prices[1:]) - min_val

        for i, val in enumerate(prices[1:]):
            if val < min_val and max_d < (max(prices[i + 1:]) - val):
                min_val = val
                max_d = (max(prices[i + 1:]) - val)
        return max_d