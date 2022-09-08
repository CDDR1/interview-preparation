class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows, cols = {}, {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] in rows:
                    return False
                else:
                    rows[matrix[i][j]] = 1
                    
                if matrix[j][i] in cols:
                    return False
                else: 
                    cols[matrix[j][i]] = 1
                    
            rows, cols = {}, {}
                    
        return True

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Time used: 9min
# Pattern: Arrays & Hashing