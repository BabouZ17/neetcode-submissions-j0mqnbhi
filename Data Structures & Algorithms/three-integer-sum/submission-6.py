class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        last_valid = []

        for i in range(0, len(nums)):
            previous = {}
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    target = -(nums[i] + nums[j])
                    if (
                        target in previous.keys()
                        and i != j != previous[target]
                        and [nums[i], nums[j], target] not in result
                        and (
                            set([nums[i], nums[j], target])
                            not in [set(val) for val in result]
                        )
                    ):
                        last_valid = [nums[i], nums[j], target]
                        result.append(last_valid)

                previous[nums[j]] = j

        return result
