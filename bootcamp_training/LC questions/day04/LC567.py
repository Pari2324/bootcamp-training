#permutation in string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # s1 aur first window ki frequency
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # First window check
        if count1 == count2:
            return True

        left = 0

        # Sliding Window
        for right in range(len(s1), len(s2)):

            # New character add
            count2[ord(s2[right]) - ord('a')] += 1

            # Old character remove
            count2[ord(s2[left]) - ord('a')] -= 1

            # Move left pointer
            left += 1

            # Compare frequencies
            if count1 == count2:
                return True

        return False
        