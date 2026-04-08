class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = currSum = 0
        for r in range(len(arr)):
            currSum += arr[r]
            if r >= k - 1:
                res += currSum / k >= threshold
                currSum -= arr[r - k + 1]
        return res