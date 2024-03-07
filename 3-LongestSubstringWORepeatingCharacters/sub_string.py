from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This algo should be a sting sliding-window problem.
        :param s: the sting.
        :return: the number of unique.
        """
        indices: dict = {}
        maxLength: int = 0
        slider: int = 0 # start sliding window

        for i, char in enumerate(s):
            if char in indices and indices[char] >= slider:
                slider = indices[char] + 1
            else:
                maxLength = max(maxLength, i - slider + 1)

            indices[char] = i

        return maxLength

# The time complex is O(n).

