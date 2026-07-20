class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total_num = high - low + 1
        if low % 2 == 1 or high %2 == 1:
            return (total_num + 1)//2
        else:
            return (total_num)//2
