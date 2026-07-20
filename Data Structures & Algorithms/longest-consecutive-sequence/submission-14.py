class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # My initial struggle was figuring out how to continue the sequence
        # after finding its starting number.
        #
        # The next consecutive value may appear anywhere in the original array,
        # so moving to the next index does not work. Instead, we look up each
        # next value directly using a set.
        #
        # Set membership is O(1) on average, while searching for a value in an
        # array takes O(n).
        #
        # A number starts a sequence only if num - 1 is not in the set.
        # From that starting point, keep checking currentNum + 1 until the
        # sequence ends.
        #
        # Iterate over the set so duplicate values are processed only once.

        numSet = set(nums)
        longest = 0
        for num in numSet: # O(n)
            if num - 1 not in numSet: # O(1)
                current = num
                sequence = 1
                while current + 1 in numSet: # O(n)
                    sequence += 1
                    current += 1
                longest = max(longest, sequence)
        return longest

    # Pattern: Set
    # Time: O(n)
    #   - The inner loop shares the same set of elements
    # Space: O(n)


        

        