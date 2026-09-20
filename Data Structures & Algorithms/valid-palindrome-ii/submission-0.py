class Solution:

    def is_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return self.is_palindrome(s, i + 1, len(s) - 1 - i) or self.is_palindrome(s, i, len(s) - 2 - i)
        return True