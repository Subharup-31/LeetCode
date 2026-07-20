class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value = 0
        for i in accounts:
            add = 0
            for j in i:
                add += j
                max_value = max(max_value,add)

        return max_value 
                
        