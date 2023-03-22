class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            v = target-nums[i]
            if v in nums and not nums.index(v) == i:
                return i, nums.index(v)
                