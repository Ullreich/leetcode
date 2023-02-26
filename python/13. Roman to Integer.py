class Solution:
    def romanToInt(self, s: str) -> int:
        interpret = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum([interpret[i] if interpret[i] >= interpret[j] else -interpret[i] for i, j in zip(s, s[1:] + "I")])