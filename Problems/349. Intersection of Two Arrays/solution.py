class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        map = {}
        
        for num in nums1:
            map[num] = True
            
        for num in nums2:
            if num in map:
                result.append(num)
                map.pop(num)
                
        return result

# Time Complexity: O(m + n)
# Space Complexity: O(n)
# Time used: 16min