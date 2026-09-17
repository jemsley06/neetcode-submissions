class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freqs1 = {}
        freqs2 = {}
        for char in s1:
            freqs1[char] = 1 + freqs1.get(char, 0)
        if len(s1) > len(s2):
            return False
        for r in range(len(s2)):
            freqs2[s2[r]] = 1 + freqs2.get(s2[r], 0)
            if r - l > len(s1) - 1:
                freqs2[s2[l]] = -1 + freqs2.get(s2[l])
                if freqs2[s2[l]] == 0:
                    del freqs2[s2[l]]
                l+=1
            if freqs1 == freqs2:
                return True
        return False

            
            