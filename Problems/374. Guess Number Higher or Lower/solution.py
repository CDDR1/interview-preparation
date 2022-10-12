# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # initial range = 1 to n
        # l = 6
        # r = 10
        # currGuess = 5
        # first guess: n // 2
        # next guesses: (n - l) // 2
        
        l = 1
        r = n
        currGuess = n // 2
        
        while (l <= r):
            check = guess(currGuess)
            if check == -1:
                r = currGuess - 1
                currGuess = l + (r - l) // 2
            elif check == 1:
                l = currGuess + 1
                currGuess = l + (r - l) // 2
            else:
                return currGuess

# Time complexity: O(log n)
# Space complexity: O(1)
# Pattern: Binary Search
# Time used: 16min