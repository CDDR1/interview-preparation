class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows, cols = set(), set()
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                rows.add(matrix[i][j])
                cols.add(matrix[j][i])
            if len(rows) != n or len(cols) != n:
                return False
            rows, cols = set(), set()
        
        return True
                
# Solution using Sets instead of HashMaps, which is the suggested way of solving it according to LeetCode's hints.