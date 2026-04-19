class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        res = list(s)

        for direction, amount in shift:
            amount = amount % len(s)
            while amount:
                if direction: # right
                    res = [res[-1]] + res[:-1]
                else: # left
                    res = res[1:] + [res[0]]
                amount -= 1
        return "".join(res)