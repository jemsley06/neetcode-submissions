class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(piles, h, k):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            return hours <= h
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(piles, h, mid):
                hi = mid        # mid works; answer is mid or smaller
            else:
                lo = mid + 1    # too slow; need faster
        return lo