class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a dictionary to store the current number and index. For each number,
        # check if target - nums[i] exist in the dictionary.
        seen = {}

        for i in range(len(nums)): # O(n)
            diff = target - nums[i]
            if diff in seen: # O(1)
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
        return []

        # Pattern: dictionary
        # Time: O(n)
        # Space: O(n)
        


        