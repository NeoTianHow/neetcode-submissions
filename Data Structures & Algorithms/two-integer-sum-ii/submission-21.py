class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers because the array is sorted.
        # Move the left pointer if the sum is too small,
        # Move the right pointer left if the sum is too large.

        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1

        return []

    # Pattern: Two Pointers
    # Time: O(n)
    #   - Each pointer moves across the array at most once.
    # Space: O(1)