class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remainders = {}

        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if remainder in remainders.keys():
                return [remainders[remainder], i + 1]
            remainders[numbers[i]] = i + 1

        return remainders