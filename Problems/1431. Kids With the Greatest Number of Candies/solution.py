class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        for candy in candies:
            greatest = max(greatest, candy)
          
        ans = []
        for candy in candies:
            if candy + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays