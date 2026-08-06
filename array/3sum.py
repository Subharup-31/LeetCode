class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        # both i and j should be inside the loop because every new k axts as a reset to i and j
        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1

            if k != 0:
                if nums[k] == nums[k - 1]:
                    continue

            while i < j:
                # j!=k i!=j and i!=k are unnecessary because the pointers always start at different indices
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