class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hashset = set()

        for i in range(len(nums)-1):
            sum = nums[i] + nums[i+1]
            if sum in hashset:
                return True
            else:
                hashset.add(sum)
        return False        
        