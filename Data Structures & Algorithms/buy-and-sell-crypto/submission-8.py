class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window of buy then sell
        # when to extend?
        # when to shift L
        # always extend right but if prices[r] < prices[l] then record profit and switch

        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if prices[r] < prices[l]:
                l = r
        return max_profit