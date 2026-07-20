class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hashmap1 = {}
        hashmap2 = {}
        s = s.split()
        character = list(pattern)

        if len(character) != len(s):
            return False

        for i,j in zip(character,s):
            if i not in hashmap1:
                hashmap1[i] = j
            else:
                if hashmap1[i]!= j:
                    return False

            if j not in hashmap2:
                hashmap2[j] = i
            else:
                if hashmap2[j] != i:
                    return False
                
        return True

        
  