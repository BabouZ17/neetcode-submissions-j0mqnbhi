from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = Counter(nums)
        result = []

        return [val[0] for val in occurences.most_common(k)]

        # occurences = {value: 0 for value in list(set(nums))}
        # result = []
        
        # for num in nums:
        #     occurences[num] += 1
        #     if occurences[num] == k:
        #         result.append(num)
        # return result
        

        