class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums: List[int], s: int, m: int, e: int):
            L, R = nums[s: m+1], nums[m+1: e+1]
            i = j = 0
            k = s

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1 

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

        def merge_sort(nums: List[int], s: int, e: int) -> List[int]:
            if e == s:
                return nums

            m = (s+e)//2
            merge_sort(nums, s, m)
            merge_sort(nums, m+1, e)

            merge(nums, s, m, e)
            return nums
        return merge_sort(nums, 0, len(nums) - 1)