class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in t:
            if j in hashmap:
                hashmap[j] -= 1
            else:
                return False
                
            if hashmap[j] < 0:
                return False
        return True

        # other way is
        # for values in hashmap.values():
        #     if values != 0:
        #         return False
        # return True