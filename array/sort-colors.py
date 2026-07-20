class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        high = len(nums)-1
        current = 0

        while high >= current:
            if nums[current] == 0:
                nums[low],nums[current] =nums[current],nums[low]
                low += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[high],nums[current] = nums[current],nums[high]
                high -= 1

        