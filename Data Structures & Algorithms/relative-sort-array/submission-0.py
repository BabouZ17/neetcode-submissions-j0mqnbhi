from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        i = 0

        for num in arr2:
            while counts[num] > 0:
                arr1[i] = num
                counts[num] -= 1
                i += 1

        remaining = sorted(counts.elements())
        arr1[i:] = remaining
        return arr1