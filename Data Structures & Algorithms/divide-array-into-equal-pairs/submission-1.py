class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
    
        for cnt in counts.values():
            if cnt % 2 == 1:
                return False

        return True