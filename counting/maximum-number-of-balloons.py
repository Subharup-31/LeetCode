class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        ans = min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )
        
        return ans