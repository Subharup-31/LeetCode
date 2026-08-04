class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        i = 0
        j = len(s)-1

        while i < j:
            if s[i].isalnum():
                pass
            else:
                i += 1
                continue

            if s[j].isalnum():
                pass
            else:
                j -= 1
                continue

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True