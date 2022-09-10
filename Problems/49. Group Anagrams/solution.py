class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        result = []
        
        wordsChars = {}
        for word in strs:
            wordsChars[word] = {}
            for char in word:
                if char in wordsChars[word]:
                    wordsChars[word][char] += 1
                else:
                    wordsChars[word][char] = 1
        
        seenIndexes = set()
        for indexI, i in enumerate(strs):
            currWord = wordsChars[i]
            currGroup = []
                    
            for indexJ, j in enumerate(strs):
                if indexJ in seenIndexes:
                    continue
                if indexJ != indexI and currWord == wordsChars[j]:
                    currGroup.append(j)
                    seenIndexes.add(indexJ)
                
            if indexI not in seenIndexes:
                currGroup.append(i)
                result.append(currGroup)
            
            seenIndexes.add(indexI)
            
        return result

# Time Used: 91min
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Pattern: Arrays & Hashing