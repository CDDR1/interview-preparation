class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else: 
                count[s[r]] = 1
                
            windowSize = r + 1 - l
            
            # I don't understand how this is less efficient
            # than the max(count.values()). The time complexity
            # of both should be O(n)
        
            # mostFrequent = 1
            # for i in range(l, r):
            #     if count[s[i]] > mostFrequent:
            #         mostFrequent = count[s[i]]
            
            mostFrequent = max(count.values())
                    
            
            while windowSize - mostFrequent > k:
                count[s[l]] -= 1
                l += 1
                windowSize -= 1
            
            ans = max(ans, windowSize)
            
                
        return ans
    
    # Time Complexity: O(n * windowSize) 
    # According to NeetCode this is O(n) but not to me
    # Space complexity: O(n)
    # Pattern: Sliding Window
    # Used NeetCode's video to solve this question
    
    
    