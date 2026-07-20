class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0

        for i in costs:
           
            if i > coins:
                break
            
            coins -= i
            count +=1

        return count