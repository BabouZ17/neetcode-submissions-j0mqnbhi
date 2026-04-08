class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            current_sum = numbers[l] + numbers[r]

            if target < current_sum:
                r -= 1
            elif target > current_sum:
                l += 1
            else:
                return [l+1, r+1]