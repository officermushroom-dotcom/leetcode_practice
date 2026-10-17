class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in d:
                return [d[pair], i]
            d[nums[i]] = i