class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        # Solution:
        # - iterate over the array of strings
        # - for each string, use two pointers to check if it is a palindrome
        # - Two pointers explanation: l = start of string (0), r = last index in the string (len(string) - 1)
        # - increment l and decrement r until they meet. In each iteration, l has to be equal to r for the string to be
        #   a valid palindrom
        
        #                i
        # ["abc","car","ada","racecar","cool"]
        
        # "ada"
        #    l 
        #  r
        
        for word in words:
            l = 0
            r = len(word) - 1
            while (l <= r):
                if word[l] != word[r]:
                    break
                l += 1
                r -= 1
            if l > r:
                return word
        return ""
    
# Time complexity: O(n*m), where n is the length of the words array and m is the length of each word
# Space complexity: O(1)
# Pattern: Two Pointers
# Time used: 9mins