class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 -1
        min_int = -(2**31) 

        reverse = 0
        if x < 0 :
            x = abs(x)
            while x != 0:
                reverse = (reverse * 10) + (x % 10)
                x = x // 10
            return -reverse if min_int <= -reverse <= max_int else 0
        elif x > 0 :
            while x != 0:
                reverse = (reverse * 10) + (x % 10)
                x = x // 10
            return reverse if min_int <= reverse <= max_int else 0

        return 0