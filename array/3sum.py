class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1

            if k != 0:
                if nums[k] == nums[k - 1]:
                    continue

            while i < j:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif current_sum < 0:
                    i += 1

                else:
                    j -= 1

        return ans