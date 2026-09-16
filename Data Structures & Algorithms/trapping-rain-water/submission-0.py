class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        i, j = 0, len(height) - 1
        totalwater = 0
        waterlevel = 0
        while i < j:
            totalwater += 0 if height[i] > waterlevel else waterlevel - height[i]
            totalwater += 0 if height[j] > waterlevel else waterlevel - height[j]
            waterlevel = max(waterlevel, min(height[i], height[j]))
            if height[i] < height[j]:
                i+=1
            else: 
                j-=1
        return totalwater