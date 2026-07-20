class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = Counter(nums)

        for key,value in hashmap.items():
            if value >= 2:
                return key
        