class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = list(), list()
        for num in nums:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)

        idx = 0
        for e in even:
            nums[idx] = e
            idx += 1
        for o in odd:
            nums[idx] = o
            idx += 1
        return nums