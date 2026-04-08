class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        return [val[0] for val in sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]]