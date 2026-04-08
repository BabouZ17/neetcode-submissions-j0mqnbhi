class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = currSum = 0
        for r in range(len(arr)):
            currSum += arr[r]
            if r >= k - 1:
                res += currSum >= threshold
                currSum -= arr[r - k + 1]
        return res