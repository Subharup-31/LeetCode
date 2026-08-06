class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        #both i and j shodul be inside the j loop cause when k moves forward everyhting shoudl resets
        for k in range(len(nums)-2):
            i = k+1
            j = len(nums)-1
            if k != 0:
                if nums[k] == nums[k-1]:
                    continue 
            while i < j :
                # here j!= k and i!=j and i!=k is not reqired as from starting we are pointing 3 pointer in different possitions so it is always gareenteed
                current_sum = nums[i]+nums[j]+nums[k]
                if current_sum == 0 :
                    ans.append([nums[i],nums[j],nums[k]])    
                    i += 1
                    j -= 1
                elif current_sum < 0:
                    i += 1
                elif current_sum > 0:
                    j -= 1
        return ans
                 