class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        currSum = sum(arr[:k-1])

        for l in range(len(arr) - k + 1):
            currSum += arr[l + k - 1]
            if currSum / k >= threshold:
                res += 1
            currSum -= arr[l]
        return res