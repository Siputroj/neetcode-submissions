class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        start = 0
        end = len(s) - 1
        for _ in range(len(s) // 2):
            if s[start] == '(' and s[end] != ')':
                return False
            elif s[start] == '{' and s[end] != '}':
                return False
            elif s[start] == '[' and s[end] != ']':
                return False

        return True
        