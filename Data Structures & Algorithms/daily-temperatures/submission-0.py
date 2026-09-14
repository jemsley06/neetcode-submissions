class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][1]:
                stack.append([i, temp])
            if temp > stack[-1][1]:
                while stack:
                    if temp <= stack[-1][1]:
                        break
                    day = stack.pop()
                    result[day[0]] = i - day[0]
                stack.append([i, temp])
        return result
