def countGoodSubstrings(self, s: str) -> int:
        # input: s = "aababcab"
        
        # Edge cases: 
        # - all chars are the same: "aaaaa"
        # - length of s is less than 3
        
        # Brute force solution
        # - loop over the string
        # - in each iteration, create an inner loop that does 3 iterations
        # - inside the inner loop, add the current character to the set in each iteration
        # - after the inner loop, check if the length of the set is 3. If it is, increment counter
        # - clear set
        
        seen = set()
        counter = 0
        
        for i in range(len(s) + 1 - 3):
            for j in range(i, i + 3):
                seen.add(s[j])
            if len(seen) == 3:
                counter += 1
            seen.clear()
            
        return counter


# Time complexity: O(3n), can be reduced to O(n) using sliding window
# Space complexity: O(n)
# Pattern: supposed to be solved with a sliding window. Here I just used a set.
# Time used: about 20mins