class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_idx, _ = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((i, temp))
        return res