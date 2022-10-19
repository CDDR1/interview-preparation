class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        greatest = -1
        
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = greatest
            greatest = max(greatest, arr[i])
            
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays
# Time used: 15min