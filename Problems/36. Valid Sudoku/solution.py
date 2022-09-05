class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        box1 = {}
        box2 = {}
        box3 = {}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in rows:
                    return False
                elif board[i][j] != "." and board[i][j] not in rows:
                    rows[board[i][j]] = 1
                    
                if board[j][i] in cols:
                    return False
                elif board[j][i] != "." and board[j][i] not in cols:
                    cols[board[j][i]] = 1
                
                if j < 3:
                    if board[i][j] in box1:
                        return False
                    elif board[i][j] != "." and board[i][j] not in box1:
                        box1[board[i][j]] = 1
                elif j < 6:
                    if board[i][j] in box2:
                        return False
                    elif board[i][j] != "." and board[i][j] not in box2:
                        box2[board[i][j]] = 1
                else:
                    if board[i][j] in box3:
                        return False
                    elif board[i][j] != "." and board[i][j] not in box3:
                        box3[board[i][j]] = 1
          
            if i == 2 or i == 5:
                box1 = {}
                box2 = {}
                box3 = {}
                
            rows = {}
            cols = {}
                
                
        return True
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# 72 min used