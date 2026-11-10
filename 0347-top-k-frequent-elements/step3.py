from collections import Counter


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
    