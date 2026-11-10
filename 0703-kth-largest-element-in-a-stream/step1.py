import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap_nums = nums.copy()
        heapq.heapify(self.heap_nums)
        self.k = k
        while len(self.heap_nums) > k:
            heapq.heappop(self.heap_nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_nums, val)
        if len(self.heap_nums) > self.k:
            heapq.heappop(self.heap_nums)
        return self.heap_nums[0]
    