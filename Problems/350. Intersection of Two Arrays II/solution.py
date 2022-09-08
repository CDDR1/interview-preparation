class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1, map2 = {}, {}
        result = []
        
        for i in nums1:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1
                
        for i in nums2:
            if i in map2:
                map2[i] += 1
            else:
                map2[i] = 1
                
        seen = set()
        for i in nums1:
            if i in map1 and i in map2 and i not in seen:
                min = 0
                if map1[i] > map2[i]:
                    min = map2[i]
                else:
                    min = map1[i]
                for j in range(min):
                    result.append(i)
                seen.add(i)
                    
        return result
    
# Time Complexity: O(m + n * (inner for loop))  ...not sure about this one
# Space Complexity: O(m + n) ...again, not very sure
# Time used: 40min
# Pattern: Arrays & Hashing