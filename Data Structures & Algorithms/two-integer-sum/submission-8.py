class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in m.keys():
                return [m[d], i]
            else:
                m[nums[i]] = i