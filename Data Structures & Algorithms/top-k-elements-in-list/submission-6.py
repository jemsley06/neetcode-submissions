from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        inorder = num_counts.most_common()
        r = []
        for i in range(k):
            r.append(inorder[i][0])
        return r