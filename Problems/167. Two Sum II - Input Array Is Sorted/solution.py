class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while (l < r):
            if (numbers[l] + numbers[r] == target):
                return [l + 1, r + 1]
            if (numbers[l] + numbers[r] > target):
                r -= 1
            elif (numbers[l] + numbers[r] < target):
                l += 1
                
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time used: 9min
# Pattern: Two Pointers