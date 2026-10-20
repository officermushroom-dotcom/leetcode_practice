class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sorted_nums1 = nums1.sort()
        sorted_nums2 = nums2.sort()
        i, j = 0, 0
        result = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return list(result)
    