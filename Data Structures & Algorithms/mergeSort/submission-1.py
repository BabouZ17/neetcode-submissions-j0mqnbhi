# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(pairs, s, m, e):
            L = pairs[s: m + 1]
            R = pairs[m + 1: e + 1]

            i = 0 # pointer for left side
            j = 0 # pointer for right side
            k = s # pointer for pairs

            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    i += 1
                else:
                    pairs[k] = R[j]
                    j += 1
                k +=1

            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                pairs[k] = R[j]
                j += 1
                k += 1

        def merge_sort(pairs, s, e):
            if e - s <= 0:
                return pairs

            m = (s + e) // 2

            merge_sort(pairs, s, m)
            
            merge_sort(pairs, m + 1, e)

            merge(pairs, s, m, e)
        
            return pairs
        
        return merge_sort(pairs, 0, len(pairs))