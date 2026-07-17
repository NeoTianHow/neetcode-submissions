class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Two passes: build prefix products, then multiply by postfix products.
        prefix = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
    
    # Pattern: Prefix & Suffix Products
    # Time: O(n)
    # Space: O(1) auxiliary space (output array not counted)