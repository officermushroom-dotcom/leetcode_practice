from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_s_to_anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            sorted_s_to_anagrams[sorted_s].append(s)
        return list(sorted_s_to_anagrams.values())
    