class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if flowerbed[i] == 0:
                if i - 1 < 0:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue
                if i + 1 >= len(flowerbed):
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue
                if (flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                
        return True if n == 0 else False
    
    
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays
# Time used: 13min