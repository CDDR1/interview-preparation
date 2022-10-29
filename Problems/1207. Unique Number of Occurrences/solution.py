class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for num in arr:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
                
        nums = set()
        freqs = set()
        for num in arr:
            if map[num] in freqs and num not in nums:
                return False
            freqs.add(map[num])
            nums.add(num)
            
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Time used: 7min