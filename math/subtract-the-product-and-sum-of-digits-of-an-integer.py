class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        add = 0
        while n > 0:
            i = n%10
            n = n // 10  
            product *= i
            add += i

        return product - add
        