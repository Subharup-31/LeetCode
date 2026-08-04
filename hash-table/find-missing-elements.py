class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        i = 0 
        while i < (len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                i += 1
                continue
            else:
                for j in range(nums[i]+1,nums[i+1]):
                    ans.append(j)
                i += 1

        return ans
        