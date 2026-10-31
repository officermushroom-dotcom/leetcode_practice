class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_parts = ['(', '[', '{']
        for c in s:
            if c in left_parts:
                stack.append(c)
                continue
            if not stack:
                return False
            top = stack.pop()
            if top == '(':
                if c != ')':
                    return False
            if top == '[':
                if c != ']':
                    return False
            if top == '{':
                if c != '}':
                    return False
        return len(stack) == 0
