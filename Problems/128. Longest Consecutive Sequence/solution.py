class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for i in nums:
            currLongest = 0
            if i - 1 not in numSet:
                    currLongest += 1
                    while i + 1 in numSet:
                        currLongest += 1
                        i += 1
            if currLongest > longest:
                longest = currLongest
                
        return longest
    
# Time Complexity: O(n) "According to NeetCode"
# Space Complexity: O(n)
# Time used before watching NeetCode's explanation video: 82min
# Time used after watching NeetCode's video: 7min
# Pattern: Arrays & Hashing