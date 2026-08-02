class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
            else:
                hashmap[i] = 1

    
        for val in hashmap.values():
            if val != 0:
                return False
        return True