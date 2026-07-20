class Solution:
    def maxDistinct(self, s: str) -> int:
        # key thing to observe the maximum distict substring possible is always the len of uniques elements
        # each substring must start with a distinct character
        return len(set(s))
        