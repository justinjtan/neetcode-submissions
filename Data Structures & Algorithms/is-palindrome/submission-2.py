class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in list(s) if char.isalnum())
        print(s)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True