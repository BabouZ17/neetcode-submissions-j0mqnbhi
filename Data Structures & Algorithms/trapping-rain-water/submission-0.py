class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0
        
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        total = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
        return total