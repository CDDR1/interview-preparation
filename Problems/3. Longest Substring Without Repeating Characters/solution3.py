class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        longest = 0
        
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, len(seen))
        
        return longest

# The cool thing about this solution is that we're using the length of the set
# to compare and get the length of "longest", which is the variable that we
# return at the end. 