class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        curr, ans = set(nums[0]), set()
        
        for i in range(1, len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in curr:
                    ans.add(nums[i][j])
            curr = ans.copy()
            ans.clear()
            
        return list(sorted(curr))
        
        
        
# Time complexity: O(n * m)
# Space complexity: O(m)
# Pattern: Hashing
# TIm used: 31min