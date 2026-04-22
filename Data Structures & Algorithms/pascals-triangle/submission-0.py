class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for level in range(1, numRows):
            currLevel = [1] * (level + 1)
            for i in range(1, len(currLevel) - 1):
                currLevel[i] = res[-1][i - 1] + res[-1][i]
            res.append(currLevel)
        return res
