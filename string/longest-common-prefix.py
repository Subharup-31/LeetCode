class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        string1 = strs[0]
        for i in range(len(string1)):
            for s in strs:
                if  i == len(s) or s[i] != string1[i]:
                    return res
            res += string1[i]
        return res

