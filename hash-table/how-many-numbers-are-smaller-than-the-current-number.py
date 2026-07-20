class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        hashmap = {}
        res = []
        for i in range(len(temp)):
            if temp[i] not in hashmap:
                hashmap[temp[i]] = i 
                        
        for i in nums:
            res.append(hashmap[i])
        return res