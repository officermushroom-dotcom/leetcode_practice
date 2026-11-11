import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        sum_heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum_val = nums1[i] + nums2[j]
                heapq.heappush(sum_heap, (sum_val, [nums1[i], nums2[j]]))
        result = []
        for _ in range(k):
            sum_val, pair = heapq.heappop(sum_heap)
            result.append(pair)
        return result
 