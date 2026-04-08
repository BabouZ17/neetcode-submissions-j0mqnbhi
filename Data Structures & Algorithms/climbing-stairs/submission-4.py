class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1 1
        # n = 2 1 1 or 2
        # n = 3 1 1 1 or 2 1 or 1 2

        if n <= 1:
            return n

        dp = [0, 1]
        for i in range(n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1]