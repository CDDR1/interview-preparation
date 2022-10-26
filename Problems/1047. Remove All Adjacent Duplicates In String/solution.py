class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        n = len(s)
        for i in range(n - 1, -1, -1):
            if (i == n - 1) or (not stack):
                stack.append(s[i])
                continue
            
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
                
        ans = ""
        while stack:
                ans += stack.pop()
                
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Stack
# Time used: 29min