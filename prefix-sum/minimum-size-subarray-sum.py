class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        min_lenght = float('inf')
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                curr_sum -= nums[left]
                min_lenght = min(min_lenght,right-left+1)
                left += 1

        if min_lenght == float('inf'):
            return 0
        return min_lenght
                

                
