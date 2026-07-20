class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # a better approch is to conver to a list as list are immutable
        #python creates a new string everytime i add

        res = []
        i = 0 
        j = 0
        arr1 = list(word1) 
        arr2 = list(word2)
        while i < len(arr1) and j < len(arr2):
            res.append(arr1[i])
            res.append(arr2[j])

            i += 1
            j += 1

        res.extend(arr1[i:])
        res.extend(arr2[j:])

        return "".join(res)