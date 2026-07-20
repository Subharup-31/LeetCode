class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force approch will give O(n2), two pointers gives O(n)
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                # condition where both are equal, either of it can be incremented
                left += 1

        return res
