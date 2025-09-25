# Roman
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        previous = 0
        values = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
        for char in reversed(s):
            if values[char] >= previous:
                total += values[char]
            else:
                total -= values[char]
            previous = values[char]
        return total


# prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
