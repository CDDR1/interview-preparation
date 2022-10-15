# BRUTE FORCE APPROACH
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        for i in range(len(nums2)):
            map[nums2[i]] = -1
            for j in range(i, len(nums2)):
                if i < j and nums2[j] > nums2[i]:
                    map[nums2[i]] = nums2[j]
                    break
                    
        ans = []
        for num in nums1:
            ans.append(map[num])
            
        return ans
    
# Time Complexity: O(n + m^2), n being the length of nums1 and m being the length of nums2
# Space Complexity: O(n), because we're using a HashMap
# Pattern: Arrays & Hashing
# Time used: about 12min