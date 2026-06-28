class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        y = x[-1]
        length = len(y)
        return length
