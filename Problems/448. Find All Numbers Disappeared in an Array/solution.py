class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if n == 1:
            return [nums]
        
        map = {}
        for num in nums: 
            map[num] = True
            
        result = []
        for i in range(n):
            if n - i not in map: 
                result.append(n - i)
                
        return result
        
        
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time used: about 20 or 25 minutes. Not sure, solved it on a train lol
# Pattern: Arrays & Hashing