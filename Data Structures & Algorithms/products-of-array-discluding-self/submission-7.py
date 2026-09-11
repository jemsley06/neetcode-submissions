class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            pre[i] = product
        i = len(nums) - 1
        product = 1
        while i >= 0:
            product *= nums[i]
            suf[i] = product
            i-=1
        for i in range (len(nums)):
            if i == 0:
                output.append(suf[i + 1])
            elif i == len(nums) - 1:
                output.append(pre[i - 1])
            else:
                output.append(pre[i - 1] * suf[i + 1])
        return output

