class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        map = {}   
        str = ""
        result = []
        words = []
        
        for i in range(len(s1) + 1):
            if i == len(s1) or s1[i] == " ":
                words.append(str)
                str = ""
            else:
                str += s1[i]
            
        for i in range(len(s2) + 1):
            if i == len(s2) or s2[i] == " ":
                words.append(str)
                str = ""
            else:
                str += s2[i]
            
        for i in words:
            if i in map:
                map[i] += 1
            else: 
                map[i] = 1
                
        for i in words:
            if map[i] == 1:
                result.append(i)
                
        return result
    
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Time Used: 48 min