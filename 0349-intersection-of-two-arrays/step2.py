class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            bigger_nums = nums1
            smaller_nums = nums2
        else:
            bigger_nums = nums2
            smaller_nums = nums1
        set_nums = set(smaller_nums)

        result = set()

        for num in bigger_nums:
            if num in set_nums:
                result.add(num)
        return list(result)
        

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
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
