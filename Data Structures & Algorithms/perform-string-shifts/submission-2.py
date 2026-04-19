class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shifts, right_shifts = 0, 0

        for direction, amount in shift:
            if direction:
                right_shifts += amount
            else:
                left_shifts += amount
        
        if left_shifts == right_shifts:
            return s

        direction = 1 if left_shifts > right_shifts else -1
        count = abs(left_shifts - right_shifts)
        count %= len(s)

        res = s[direction * count:] + s[:direction * count]
        return "".join(res)