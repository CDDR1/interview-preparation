# Apparently this solution is invalid because we are not supposed to 
# use any additional data structures to store the strings.

class Solution:
    
    def __init__(self):
        self.encoded, self.decoded = {}, {}

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        self.encoded[tuple(strs)] = ""

        for index, s in enumerate(strs):
           self.encoded[tuple(strs)] += s 
           if index < len(strs) - 1:
               self.encoded[tuple(strs)] += "$" 

        self.decoded[self.encoded[tuple(strs)]] = strs
        
        return self.encoded[tuple(strs)]

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        return self.decoded[str]

# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Arrays & Hashing
# Time used: 16min

 