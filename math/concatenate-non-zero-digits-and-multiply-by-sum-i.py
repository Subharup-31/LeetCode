class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0
        res = []

        for i in str(n):
            if i == '0':
                continue
            else:
                res.append(i)

        x = "".join(res)
        print(x)
        add =0
        for i in res:
            add += int(i)
        return add * int(x)
