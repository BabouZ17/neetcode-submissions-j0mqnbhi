from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}

        for num in nums:
            occurences.update({num: 1 + occurences.get(num, 0)})

        sorted_occurences = sorted(occurences.items(), key=lambda val: val[1], reverse=True)
        result = []

        for i, val in enumerate(sorted_occurences):
            result.append(val[0])
            if i + 1 == k:
                return result
        

        