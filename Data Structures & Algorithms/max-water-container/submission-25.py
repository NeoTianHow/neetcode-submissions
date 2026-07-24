class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start with pointers at both ends to get the maximum width.
        # Calculate the container area, then move the pointer at the
        # shorter bar inward to look for a taller bar.

        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            water = width * height

            maxWater = max(maxWater, water)

            # Move the shorter bar because keeping it cannot increase
            # the area, while the width will only become smaller.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxWater

    # Pattern: Two Pointers
    # Time: O(n)
    #   - Each pointer moves across the array at most once.
    # Space: O(1)