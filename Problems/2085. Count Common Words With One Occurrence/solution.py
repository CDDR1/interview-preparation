class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        counter = 0
        
        seen1 = {}
        seen2 = {}
        
        for word in words1:
            if word in seen1:
                seen1[word] = seen1[word] + 1
            else:
                seen1[word] = 1
                
        for word in words2:
            if word in seen2:
                seen2[word] = seen2[word] + 1
            else: 
                seen2[word] = 1
                
        for word in words1:
            if word in seen1 and word in seen2 and seen1[word] == 1 and seen2[word] == 1:
                counter = counter + 1
                
        return counter

# Time Complexity: O(m + n)
# Space Complexity: O(m + n)
# Time used: 16min