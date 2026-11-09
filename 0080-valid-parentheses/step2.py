class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(': ')', '[': ']', '{': '}'}
        open_brackets = []
        for c in s:
            if c in open_to_close:
                open_brackets.append(c)
                continue
            if open_brackets:
                latest_bracket = open_brackets.pop()
                if open_to_close[latest_bracket] == c:
                    continue
            return False
        return not open_brackets
    