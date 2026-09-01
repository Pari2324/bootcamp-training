#first unique character in a string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        # Frequency count
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # First unique character
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
        