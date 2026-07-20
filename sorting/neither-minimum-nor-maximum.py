class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if len(nums)<3:
                return -1
            else:
                return nums[-2]