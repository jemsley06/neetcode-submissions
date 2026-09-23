class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        key = 0
        for i in range(len(nums)):
            key ^= (1 << nums[i])
            if (key >> nums[i]) & 1 == 0:
                return nums[i]

