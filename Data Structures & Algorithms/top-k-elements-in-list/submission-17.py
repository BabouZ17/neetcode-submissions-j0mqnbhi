from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        res = []
        i = len(count) - 1
        sort = sorted(count.items(), key=lambda x: x[1])[:]
        while k > 0:
            res.append(sort[i][0])
            k -= 1
            i -= 1
        return res