class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers starting from both ends of the string.
        # Skip non-alphanumeric characters, then compare the remaining
        # characters (case-insensitive)
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphanumeric(s[l]):
                l += 1

            while l < r and not self.isAlphanumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphanumeric(self, c: str) -> bool:
        return (
            ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
        )
    # Pattern: Two Pointers
    # Time: O(n)
    #   - Each pointer moves across the string only once.
    # Space: O(1)