from collections import Counter
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = []
        seen = {}
        for word in strs:
            l = tuple(sorted(word))
            if l not in seen:
                seen[l] = len(d)
                d.append([word])
            else:
                d[seen[l]].append(word)
        return d