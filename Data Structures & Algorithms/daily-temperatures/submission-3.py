class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day_idx, _ = stack.pop()
                res[prev_day_idx] = i - prev_day_idx
            stack.append((i, temp))
        return res