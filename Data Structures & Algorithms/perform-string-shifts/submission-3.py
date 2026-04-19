class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shifts = 0

        for direction, amount in shift:
            if direction == 0:
                shifts += amount
            else:
                shifts -= amount

        shifts %= len(s)
        res = s[shifts:] + s[:shifts]
        return "".join(res)