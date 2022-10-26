class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        nums.sort() 
        n = len(nums)
        
        for a in range(n - 2):
            if (a > 0) and (nums[a] == nums[a - 1]):
                continue
            l = a + 1
            r = n - 1
            while (l < r):
                sum = nums[a] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    triplets.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while (l < r) and (nums[l - 1] == nums[l]):
                        l += 1
                    
        return triplets

# My own solution.