class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c in ['{', '[', '(']:
                stack.append(c)
            elif c in ['}', ']', ')']:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp == '{' and c != '}':
                    return False
                elif temp == '[' and c != ']':
                    return False
                elif temp == '(' and c != ')':
                    return False
            
        if len(stack) != 0:
            return False
        else:
            return True

        