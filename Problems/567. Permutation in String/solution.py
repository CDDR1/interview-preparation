class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        count1 = {}
        count2 = {}
        
        for c in s1:
            if c in count1:
                count1[c] += 1
            else:
                count1[c] = 1
        
        for i in range(len(s1)):
            if s2[i] in count2:
                count2[s2[i]] += 1
            else:
                count2[s2[i]] = 1
        
        start = 0
        end = len(s1) - 1
        while end < len(s2):
            print(count2)
            
            counter = 0
            for c in s1:
                if c not in count2:
                    break
                    
                if count1[c] != count2[c]:
                    break
                else:
                    counter += 1
                    
                if counter == len(s1):
                    return True
                
            
            if count2[s2[start]] > 1:
                count2[s2[start]] -= 1
            elif count2[s2[start]] == 1:
                count2.pop(s2[start])
                
            start += 1
            end += 1
            
            if end >= len(s2):
                break
                
            if s2[end] in count2:
                count2[s2[end]] += 1
            else:
                count2[s2[end]] = 1
        
        return False
    
# Time complexity: O(n*len(s1))
# Space complexity: O(s1)
# Pattern: Sliding Window
# Time used: 120min
        
        