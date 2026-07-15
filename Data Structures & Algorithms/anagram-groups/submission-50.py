class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary to count the frequency for each string
        # and use it as a unique key to group similiar anagrams together.
        groups = defaultdict(list)

        for s in strs: # O(n)
            count = [0] * 26
            for i in range(len(s)): # O(k)
                count[ord(s[i]) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(s)
        return list(groups.values()) # O(n)
    
    # Pattern: Dictionary
    # Time: O(n * k)
    #   - The inner loop don't share the same set of elements
    # Space: O(n)
    #   - tuple(count) is O(1) because it always contains 26 elements.
    #   - groups is O(n) because, in the worst case, each string forms its own anagram group,
    #     resulting in up to n dictionary entries.

        