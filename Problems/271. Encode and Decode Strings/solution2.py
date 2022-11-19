class Solution:
    
    def __init__(self):
        self.encoded, self.decoded = {}, {}

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        decoded = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            decoded.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded

# Time complexity: O(n)
# Space complexity: O(1), without counting the output array (decoded) and string (encoded).