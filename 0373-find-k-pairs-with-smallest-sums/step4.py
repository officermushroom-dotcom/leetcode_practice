import heapq
from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Candidate:
    total: int
    index1: int = field(compare=False)
    index2: int = field(compare=False)


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap: list[Candidate] = []
        for index1 in range(min(k, len(nums1))):
            heapq.heappush(heap, Candidate(nums1[index1] + nums2[0], index1, 0))

        result = []
        while heap and len(result) < k:
            candidate = heapq.heappop(heap)
            index1, index2 = candidate.index1, candidate.index2
            result.append([nums1[index1], nums2[index2]])
            if index2 + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    Candidate(nums1[index1] + nums2[index2 + 1], index1, index2 + 1),
                )
        return result
    