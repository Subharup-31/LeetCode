class Solution:
    def isPalindrome(self, s: str) -> bool:

        # the issue with this solution is its taking a extra space where i can direct accept the char which is alphnum and copare that only
        

        s = s.lower()
        new_s = ""
        for ch in s:
            if ch.isalnum():
                new_s += ch

        i = 0
        j = len(new_s) - 1

        while i < j:
            if new_s[i] == new_s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True