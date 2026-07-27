class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        maxProfit = 0

        for i in range(len(prices)):
            buy = prices[j]
            sell = prices[i]

            if buy > sell:
                # If the current buy price is more expensive than today's sell price,
                # today's sell price should become the new buy price.
                j = i
            else:
                # Otherwise, calculate the profit if we sell today.
                profit = sell - buy
                maxProfit = max(maxProfit, profit)

        return maxProfit

        # Time: O(n)
        # Space: O(1)
