from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_count = 0
        for start_index in range(len(nums)):
            total_sum = 0
            for num in nums[start_index:]:
                total_sum += num
                if total_sum == k:
                    subarray_count += 1
        return subarray_count
    