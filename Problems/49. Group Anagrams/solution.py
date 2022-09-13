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
        
        groupedIndexes = set()
        for indexI, i in enumerate(strs):
            currWord = wordsChars[i]
            currGroup = []
                    
            for indexJ, j in enumerate(strs):
                if indexJ in groupedIndexes:
                    continue
                if indexJ != indexI and currWord == wordsChars[j]:
                    currGroup.append(j)
                    groupedIndexes.add(indexJ)
                
            if indexI not in groupedIndexes:
                currGroup.append(i)
                result.append(currGroup)
            
            groupedIndexes.add(indexI)
            
        return result

# Time Used: 91min
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Pattern: Arrays & Hashing