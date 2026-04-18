class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0:
            return False

        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        invalid = {2, 3, 4, 5, 7}

        original = n
        rotated = 0

        while n > 0:
            digit = n % 10
            if digit in invalid:
                return False
            
            rotated_digit = mapping[digit]
            rotated = rotated * 10 + rotated_digit

            n //= 10

        return rotated != original