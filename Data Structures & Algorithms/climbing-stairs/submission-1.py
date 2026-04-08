class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1
        # 1
        # n = 2
        # 2
        # n = 3
        # 3
        # n = 4
        # 1 + 1 + 1 + 1
        # 2+2
        # 1+1+2
        # 2+1+1
        # 1+2+1
        # 5
        if n < 4:
            return n
        
        dp = [2, 3]
        i = 4
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1
        return dp[1]