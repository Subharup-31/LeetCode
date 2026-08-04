class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) - 1

        max_area = 0

        while i < j:

            # area = lenght x breadth
            area = (j - i) * min(height[i],height[j])
            max_area = max(max_area, area)

            if height[i] <= height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1

        return max_area
