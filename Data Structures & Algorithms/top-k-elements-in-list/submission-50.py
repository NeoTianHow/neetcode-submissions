class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a dictionary to count the frequency of each number.
        # Then place each number into an array based on its frequency.
        # Traverse the bucket from highest to lowest frequency.
        count = {}

        for num in nums: # O(n)
            count[num] = count.get(num, 0) + 1
         
        buckets = [[] for i in range(len(nums) + 1)] # O(n)

        for num, cnt in count.items(): # O(n)
            buckets[cnt].append(num)
        
        res = []
        for i in range(len(buckets) - 1, - 1, -1): # O(n)
            for num in buckets[i]:
                res.append(num)
                if len(res) == k: return res

        return res

    # Pattern: Dictionary + Bucket Sort
    # Time: O(n)
    #    - The inner loop shares the same set of element
    # Space: O(n)
