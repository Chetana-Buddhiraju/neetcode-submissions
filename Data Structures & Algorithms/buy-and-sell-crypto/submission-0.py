class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        best = 0
        for n in prices:
            if n<low:
                low = n
            best = max(best, n - low)
        return best
