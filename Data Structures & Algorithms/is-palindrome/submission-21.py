class Solution:
    def isPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1

        while L < R:

            # skip special characters from left
            while L < R and not s[L].isalnum():
                L += 1

            # skip special characters from right
            while L < R and not s[R].isalnum():
                R -= 1

            # compare actual characters
            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1

        return True

        