class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        map = {}
        maxBox = 0
        
        for n in range(lowLimit, highLimit + 1):
            box = n
            if n > 9:
                n = str(n)
                sum = 0
                
                for s in n:
                    sum += int(s)
                    
                box = sum
            
            if box in map:
                map[box] += 1
            else:
                map[box] = 1
                
            maxBox = max(maxBox, map[box])
            
        return maxBox
    
# Time complexity: O(n * m)
# Space complexity: O(n)
# Pattern: HashMaps
# Time used: 17min