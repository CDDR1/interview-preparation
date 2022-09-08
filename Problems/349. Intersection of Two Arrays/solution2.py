# Solution using a SET instead of a DICT (HASHMAP)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        mySet = set()
        
        for num in nums1:
            mySet.add(num)
            
        for num in nums2:
            if num in mySet:
                result.append(num)
                mySet.remove(num)
                
        return result
                
# Time Complexity: O(n + m)
# Space Complexity: O(n)
# Pattern: Arrays & Hashing