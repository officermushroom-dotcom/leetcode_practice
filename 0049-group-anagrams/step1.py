from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sortedWord_to_originalWord = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            sortedWord_to_originalWord[key].append(word)
        return list(sortedWord_to_originalWord.values())
    