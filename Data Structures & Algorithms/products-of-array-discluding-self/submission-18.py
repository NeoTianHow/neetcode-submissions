class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Two passes: build prefix products, then multiply by postfix products.
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            # The first prefix will have a default value of 1 
            res[i] = prefix
            # Prepare for the next number
            prefix *= nums[i]
        

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            # The first postfix will have a default value of 1.
            # But, we also need to multiply it with the prefix to get
            # the final result for each position
            res[i] *= postfix
            # Prepare for the next number
            postfix *= nums[i]
        return res
    
    # Pattern: Prefix & Suffix Products
    # Time: O(n)
    # Space: O(1) auxiliary space (output array not counted)
