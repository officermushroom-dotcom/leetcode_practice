class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for u in range(i + 1, n):
                if nums[i] + nums[u] == target:
                    return [i, u]
        