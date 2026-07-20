class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        i = 0
        j = 0
        for i in range(len(a)):
            if a[i] == 0:
                continue
                
            elif a[i] != 0:
                temp=a[i]
                a[i] = a[j]
                a[j] = temp
                j = j+1
            
        