class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxx = 0
        for i in range(len(colors)):
            j = i+1
            while i<j and j<len(colors):
                if colors[i] != colors[j]:
                    x = abs(i-j)
                    if x > maxx:
                        maxx = x
                j = j+1
        return maxx