class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        for i in nums1:
            result.append(i)
        for i in nums2:
            result.append(i)
        result.sort()
        x = len(result)
        if x % 2 == 0:
            return (result[x//2] + result[(x//2 -1)])/2
        else:
            return result[x//2]
