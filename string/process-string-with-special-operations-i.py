class Solution:
    def processStr(self, s: str) -> str:

        res = []

        for char in s:
            if len(res) == 0 and (char == "*" or char == "%" or char =="#"):
                continue
            elif char == '#':
                res = res + res
            elif char == "*":
                res.pop()
            elif char == "%":
                res = res[::-1]
            else:
                res.append(char)
        
        
        return "".join(res)
        