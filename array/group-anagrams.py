class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}
        
        for char in strs:
            s = sorted(char)
            value = tuple(s)

            if value not in ans:
                ans[value] = [char]
            else:
                ans[value].append(char)

        return list(ans.values())
        