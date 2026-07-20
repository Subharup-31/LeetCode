class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        
        for i,j in zip(s,t):
            if i in hashmap1:
                if hashmap1[i] != j:
                    return False
            else:
                hashmap1[i] = j
            
            if j in hashmap2:
                if hashmap2[j] != i:
                    return False
            else:
                hashmap2[j] = i
            
        return True