class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array, use each number as a pivot, then apply two
        # pointers to find two remaining numbers and add them as sum = 0
        # Make sure to skip duplicate values.

        res = []

        # Only sort if it doesn't hurt the time complexity (n log n)
        # Since sorted, we can use 2 pointers to arrive to a solution.
        nums.sort()

        # Stop at len(nums) - 2 because we need at least two elements
        # for our pointers.
        for i in range(len(nums) - 2):

            # Since the array is sorted, if the pivot is positive,
            # every value after it is also positive, so the sum won't be 0.
            if nums[i] > 0:
                break

            # If current pivot value is the same as the previous, 
            # then we should skip it to avoid duplicates.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            pivot = nums[i]

            while l < r:
                total = pivot + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([pivot, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate left values.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values.
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res

        # Pattern: Two Pointers
        # Time: O(n²)
        # Space: O(n) due to sorting