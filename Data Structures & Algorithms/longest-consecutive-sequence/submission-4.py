from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        length = 0
        maxlen = 0
        for num in l:
            if (num - 1) not in l:
                length = 1
                while (num + 1) in l:
                    length+=1
                    num += 1
                if length > maxlen:
                    maxlen = length
        return maxlen
        
        