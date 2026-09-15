class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = [0, 0, len(nums) - 1]
        nums.sort()
        answers = []
        for i in range(len(nums)):
            j = 0
            k = len(nums) - 1
            while j < k:
                if i == j:
                    j+=1
                    continue
                if i == k:
                    k-=1
                    continue
                if nums[j] + nums[k] + nums[i] == 0:
                    answ = [nums[i], nums[j], nums[k]]
                    answ.sort()
                    if answ not in answers:
                        answers.append(answ)
                if nums[j] + nums[k] + nums[i] < 0:
                    j+=1
                else:
                    k-=1
        return answers