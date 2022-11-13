class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        
        for s in strs:
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord("a")] += 1
                
            if tuple(count) in map:
                map[tuple(count)].append(s)
            else: 
                map[tuple(count)] = [s]
                
        return map.values()
    
# Time complexity: O(n * m), where n is the length of "strs" and m is the average length of each string insde of "strs".
# Space complexity: O(n), because in the worst case scenario, there would be no anagrams.