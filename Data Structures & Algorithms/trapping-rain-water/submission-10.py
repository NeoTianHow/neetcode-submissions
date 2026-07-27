class Solution:
    def trap(self, height: List[int]) -> int:
        # Container With Most Water chooses two bars to form one large container.
        # Trapping Rain Water calculates the water above each position, then adds them together.

        # Use two pointers and track the tallest wall seen from each side.
        # Always process the side with the smaller maximum wall because it
        # is the limiting wall that determines the trapped water.
        # After updating the tallest wall, calculate the water trapped at
        # that position and add it to the answer.

        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        res = 0

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res


    # Pattern: Two Pointers
    # Time: O(n)
    # Space: O(1)