from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        alp_to_counts = Counter(s)
        for i, alp in enumerate(s):
            if alp_to_counts[alp] == 1:
                return i
        return -1
    