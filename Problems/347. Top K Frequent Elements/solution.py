class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        ans = []
        bucket = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
                
        seen = set()
        for num in nums:
            if num not in seen:
                bucket[map[num]].append(num)
                seen.add(num)
                
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                ans.append(j)
            if len(ans) == k: 
                return ans
    
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Arrays & Hashing
# Had to look at solution