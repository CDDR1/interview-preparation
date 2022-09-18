class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for index, a in enumerate(nums):
            if index > 0 and a == nums[index - 1]:
                continue 
                
            # Two Pointers
            b = index + 1
            c = len(nums) - 1
            while b < c:
                threeSum = a + nums[b] + nums[c]
                if threeSum > 0:
                    c -= 1
                elif threeSum < 0:
                    b += 1
                else:
                    result.append([a, nums[b], nums[c]])
                    b += 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
        return result

# Time complexity: O(n^2)
# Space complexity: O(1) or O(n) depending on the implementation of the sorting method
# Pattern: Two Pointers
# Time used: about 5 hours lol