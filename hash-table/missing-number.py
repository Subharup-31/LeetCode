class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= nums[i] ^ i

        return missing 
        
        

        