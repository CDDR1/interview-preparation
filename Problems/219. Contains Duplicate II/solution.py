class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for index, num in enumerate(nums):
            if num in seen: 
                if abs(seen[num] - index) <= k:
                    return True
                else:
                    seen[num] = index
            else:
                seen[num] = index
        
        return False

# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Supposedly Sliding Window but I solved it with a HashMap
# Time used: 33min
