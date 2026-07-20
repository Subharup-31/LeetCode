class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        clean = "".join(c.lower() for c in s if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz1234567890")
        print(clean)
        return clean == clean[::-1]

