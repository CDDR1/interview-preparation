class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        counter = 0
        
        for operation in operations:
            if operation == '+':
                scores.append(scores[-2] + scores[-1])
                counter += scores[-1]
            elif operation == 'D':
                scores.append(scores[-1] * 2)
                counter += scores[-1]
            elif operation == 'C':
                counter -= scores[-1]
                scores.pop()
            else:
                num = int(operation)
                scores.append(num)
                counter += num
                
        return counter
    
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Stack
# Time used: 10min