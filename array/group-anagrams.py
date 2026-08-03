class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        hashmap = {}
        ans = []
    
        for word in strs:
            key = "".join(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]


        for val in hashmap.values():
            ans.append(val)
        
        return ans