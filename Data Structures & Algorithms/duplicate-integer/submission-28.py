class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track seen numbers. If we encounter a number
        # already in the set, return true
        seen = set()
        for num in nums: # O(n)
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        # Pattern: Set
        # Time: O(n)
        # Space: O(n)
        