class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primaryNum = 0
        secondaryNum = len(mat[0]) - 1
        total = 0
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if j == primaryNum and primaryNum == secondaryNum:
                    total += mat[i][j]
                elif j == primaryNum:
                    total += mat[i][j]
                elif j == secondaryNum:
                    total += mat[i][j]
            primaryNum += 1
            secondaryNum -= 1
            
        return total

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Time used: 18mins
# Pattern: Matrix Traversal