class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            l = str(len(st))
            encoded = l + "#" + st
            s += encoded
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            strs.append(s[j+1 : j + l + 1])
            i = j + l + 1
        return strs