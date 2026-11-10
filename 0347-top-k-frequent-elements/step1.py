from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_to_frequent = defaultdict(int)
        for num in nums:
            num_to_frequent[num] += 1
        result = []
        for num, frequent in num_to_frequent.items():
            if len(result) >= k:
                heapq.heappush(result, (frequent, num))
                heapq.heappop(result)
            else:
                heapq.heappush(result, (frequent, num))
        return [num for _, num in result]
    