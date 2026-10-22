class Solution:
    def firstUniqChar(self, s: str) -> int:
        alp_to_count = {}
        for alp in s:
            if alp in alp_to_count:
                alp_to_count[alp] += 1
            else:
                alp_to_count[alp] = 1
        for i, alp in enumerate(s):
            if alp_to_count[alp] == 1:
                return i
        return -1
 