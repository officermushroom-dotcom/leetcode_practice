from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet_to_count = Counter(s)
        for i, alphabet in enumerate(s):
            if alphabet_to_count[alphabet] == 1:
                return i
        return -1
