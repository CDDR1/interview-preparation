class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        
        while (l <= r):
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l = l + 1
            r = r - 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Time used: 3min
# Pattern: Two Pointers