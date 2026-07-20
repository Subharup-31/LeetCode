class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # seen = {}
        # can be done using hashmap but as there are only 26 letter
        # using a array makes more sence, removes the overhead of hashmap mapping
        seen = []
        for i in s:
            if i in seen:
                return i
            else:
                seen.append(i)