class Solution:
    # Prefix each string with its length followed by a delimiter (#) during encoding.
    # During decoding, read the length first, then use it to extract the string.
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs: # O(n)
            res.append(str(len(s))) # O(1)
            res.append("#")
            res.append(s)
        return "".join(res)
            


    def decode(self, s: str) -> List[str]:
        # 01234567890123
        # 5#Hello5#World
        #   ^    ^              
        #   i    j

        res = []
        l = 0
        r = 1

        while l < len(s): # O(n)
            while r < len(s) and s[r] != "#": # O(n)
                r += 1
            length = int(s[l:r])
            # Move to the first character of the string
            l = r + 1
            # Move to the end of the string (+1)
            r = l + length
            res.append(s[l:r])
            # Move to the next encoded string
            l = r
        return res

    # Pattern: String manipulation
    # Time: O(n)
    #   - The inner loop shares the same set of elements
    # Space: O(n)                               



