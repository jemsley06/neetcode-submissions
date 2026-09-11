class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = Counter(list(s))
        word2 = Counter(list(t))
        if word1 == word2:
            return True
        else:
            return False