class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for num in nums2:
            if num in nums1:
                if num not in result:
                    result.append(num)
        return result
    