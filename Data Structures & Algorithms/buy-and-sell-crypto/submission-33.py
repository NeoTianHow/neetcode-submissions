class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        # Can't use two pointer for this, because there is no safe way to move the pointers.
        # For example, if you just do buy (L) > sell (R): l += 1, doesn't mean the buy entry is bad,
        # it can also be the sell was bad to begin with.


        j = 0
        buy = prices[j]
        maxProfit = 0
        for i in range(len(prices)):
            buy = prices[j]
            sell = prices[i]
            profit = sell - buy
            # we no longer have a good buy price. Let's update buy price
            # to the current sell price, since is cheaper
            if profit < 0:
                j = i
            maxProfit = max(profit, maxProfit)
        return maxProfit
            


            
        

        # Should you move the buy pointer?

# Should you move the sell pointer?

# There is no rule that tells you which one is safe to move. just because buy (L) > sell (R), doesn't mean
# the buy entry is bad, it canbe the sell is bad.

# [10, 1, 5, 6, 7, 1]
# For each buy and sell pair, calculate the profit earned.
# if the profit is the least we have seen so far, then we can safely say for sure our buy suck?

# [5,1,5,6,7,1,10]
# Visually, I can see that you buy at 7 and you sell at 1 is the best.

# can't use 2 pointer at all, because can't shiftly move.

# 5 - 1 = 4, profit is 4 dollars. Good? okay, but still need to explore.
    # sell is lower than price -> yes
    # sell is higher than price -> 

    # so when to move?


