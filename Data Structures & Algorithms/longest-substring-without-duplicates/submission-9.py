class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        maxlen = 1
        sub = {}
        for j in range(len(s)):
            if s[j] in sub and sub[s[j]] >= i:
                i = sub[s[j]] + 1
            sub[s[j]] = j
            maxlen = max(maxlen, j - i + 1)
            j+=1
        return maxlen