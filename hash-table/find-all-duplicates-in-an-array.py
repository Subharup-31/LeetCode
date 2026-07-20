class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            value = abs(i)-1
            if nums[value] < 0:
                res.append(abs(i))
            else:
                nums[value] *= -1

        return res 

        