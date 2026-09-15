class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = -1
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                break
            last = i
        
        if last == 0:
            digits[0] = 1
            digits.append(0)
        
        return digits
        #WCRT: O(N) | Space: O(1)