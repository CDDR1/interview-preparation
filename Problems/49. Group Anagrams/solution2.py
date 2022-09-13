class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            
            if sortedWord in map:
                map[sortedWord].append(word)
            else:
                map[sortedWord] = [word]
                
        return map.values()
    
# Time Complexity: O(m * nlogn)
# Spcae Complexity: O(n)
# Pattern: Arrays & Hashing