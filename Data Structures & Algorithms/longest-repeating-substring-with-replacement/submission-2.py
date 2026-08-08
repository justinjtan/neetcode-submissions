class Solution:
    def findHighestCharCount(self, char_count: dict) -> str:
        char, count = "", 0
        for key, value in char_count.items():
            if value > count:
                char = key
                count = value
        return char
        #WCRT: O(1) since char_count max size is 26 | Space: O(1)
    
    def needsReplacement(self, char_count: dict, highest_char: str, k: int, window_length: int):
        return char_count[highest_char] + k < window_length
        #WCRT: O(1) | Space: O(1)

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_curr = 0
        highest_char_count = ""
        char_count = defaultdict(int)
        for right in range(len(s)):
            char_count[s[right]] += 1
            highest_char_count = self.findHighestCharCount(char_count)
            if not self.needsReplacement(char_count, highest_char_count, k, right - left + 1):
                max_curr = max(max_curr, right - left + 1)
                continue
            #window needs to be adjusted
            for idx in range(left, right + 1):
                char_count[s[idx]] -= 1
                highest_char_count = self.findHighestCharCount(char_count)
                if not self.needsReplacement(char_count, highest_char_count, k, right - idx):
                    left = idx + 1
                    break
        return max_curr
        #WCRT: O(N) | Space: O(1)