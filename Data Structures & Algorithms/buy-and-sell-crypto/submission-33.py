class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # We cannot start from both ends because there is no safe rule
        # for deciding which pointer to move. A bad profit could be caused
        # by either a poor buying price or a poor selling price.
        
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
