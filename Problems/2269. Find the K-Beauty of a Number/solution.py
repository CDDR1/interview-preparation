class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        s = str(num)
        ans = 0
        
        for i in range(len(s) - k + 1):
            sub = s[i:k + i]
            subNum = int(sub)
            if subNum != 0 and num % subNum == 0:
                ans += 1
        
        return ans