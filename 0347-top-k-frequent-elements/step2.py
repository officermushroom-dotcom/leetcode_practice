from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_to_frequency = Counter(nums)
        top_k_frequency = []
        for num, frequency in num_to_frequency.items():
            heapq.heappush(top_k_frequency, (frequency, num))
            if len(top_k_frequency) > k:
                heapq.heappop(top_k_frequency)
        return [num for _, num in top_k_frequency]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_to_frequency = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, frequency in num_to_frequency.items():
            buckets[frequency].append(num)
        result = []
        for frequency in range(n, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
    