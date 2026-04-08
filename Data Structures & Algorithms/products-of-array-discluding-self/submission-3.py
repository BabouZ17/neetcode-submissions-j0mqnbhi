class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suf = [1] * n
        res = [1] * n

        pref[0] = suf[n-1] = 1
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pref[i] * suf[i]
        return res