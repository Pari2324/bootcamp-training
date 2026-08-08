#longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = []
        maximum = 0
        for i in s:
            while i in sub_str:
                sub_str.pop(0)
            sub_str.append(i)
            maximum = max(maximum, len(sub_str))
        return maximum
        