class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        # as no variable is used
        for _ in range(n):
            a,b = b,a+b
        
        return b