class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = target - (numbers[l] + numbers[r])

            if current_sum == 0:
                return [l + 1, r + 1]
            elif current_sum < 0:
                r -= 1
            else:
                l += 1

        return list()