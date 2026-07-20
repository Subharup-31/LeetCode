class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans =0
        i = 0 
        j = 0
        while i<len(nums1) and j<len(nums2):
                if nums1[i]<=nums2[j] and i<=j:
                    distance = j-i
                    if ans<distance:
                        ans = distance
                        print (ans)
                    j = j + 1
                else:
                    i = i+1
                    if i>j:
                        j = i

        return ans
