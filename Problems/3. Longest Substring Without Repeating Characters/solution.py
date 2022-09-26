class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = l + 1
        longest = 1
        currLongest = 1
        seen = set()
        seen.add(s[l])
        
        while l < len(s):
            if s[r] in seen:
                l += 1
                r = l + 1
                seen.clear()
                seen.add(s[l])
                longest = max(longest, currLongest)
                currLongest = 1
            else:
                currLongest += 1
                seen.add(s[r])
                r += 1
            if r == len(s):
                longest = max(longest, currLongest)
                break
                
        return longest
    
# Time complexity: O(n^2)
# Space complexity: O(n)
# Pattern: Sliding Window
# Time used: 28min