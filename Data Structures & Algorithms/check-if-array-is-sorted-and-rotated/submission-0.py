class Solution:
    def check(self, nums: List[int]) -> bool:
        candidate = nums[:]
        candidate.sort()

        for i in range(len(nums)):
            if candidate == nums:
                return True
            candidate = self.rotate(candidate)
        return False

    def rotate(self, nums: list[int]) -> list[int]:
        nums[:] = nums[-1:] + nums[:-1]
        return nums