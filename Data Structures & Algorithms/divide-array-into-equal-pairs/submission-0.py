class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        pairs = len(nums) / 2

        for num in nums:
            counts[num] += 1
            if counts[num] == 2:
                pairs -= 1
                counts[num] = 0
        
        return True if not pairs else False