from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_s_to_anagarams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            sorted_s_to_anagarams[sorted_s] = s
        return list(sorted_s_to_anagarams.values())

