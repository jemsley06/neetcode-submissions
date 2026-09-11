from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        b = []
        for i in range(len(nums) + 1):
            b.append([])
        for n in num_counts:
            b[num_counts[n]].append(n)
        ret = []
        for bucket in reversed(b):
            for num in bucket:
                ret.append(num)
                if len(ret) == k:
                    return ret
