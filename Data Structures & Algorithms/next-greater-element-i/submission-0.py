class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapPos = dict()
        result = list()

        for i in range(len(nums2)):
            mapPos[nums2[i]] = i
        
        print(mapPos)
        for num in nums1:
            nextGreat = num
            i = mapPos[num]
            while i < len(nums2):
                if nums2[i] > nextGreat:
                    nextGreat = nums2[i]
                    break
                i += 1

            result.append(nextGreat if nextGreat != num else - 1)
        return result