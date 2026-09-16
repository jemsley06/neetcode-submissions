class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 1
        bank = {}
        i = 0
        maxf = 0
        for j in range(len(s)):
            bank[s[j]] = 1 + bank.get(s[j], 0)
            maxf = max(maxf, bank[s[j]])
            while (j - i + 1) - maxf > k:
                bank[s[i]] -= 1
                i += 1
            maxlen = max(maxlen, j - i + 1)
        return maxlen
                
        

        