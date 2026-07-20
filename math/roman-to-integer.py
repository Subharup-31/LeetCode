class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {}
        res = 0  

        hashmap['I'] = 1
        hashmap['V'] = 5
        hashmap['X'] = 10
        hashmap['L'] = 50
        hashmap['C'] = 100
        hashmap['D'] = 500
        hashmap['M'] = 1000

        for i in range(len(s)):
            if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i+1]]:
                res -= hashmap[s[i]]
            else:
                res+= hashmap[s[i]]

        return res 
