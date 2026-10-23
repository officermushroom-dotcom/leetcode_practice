from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_frequency = defaultdict(int)
        prefix_sum_to_frequency[0] = 1
        current_sum = 0
        equal_k_subarrays = 0
        for num in nums:
            current_sum += num
            equal_k_subarrays += prefix_sum_to_frequency[current_sum - k]
            prefix_sum_to_frequency[current_sum] += 1
        return equal_k_subarrays
    