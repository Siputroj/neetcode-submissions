class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = None
        for token in tokens:
            try:
                int(token)
                stack.append(token)
            except:
                num_2, num_1 = stack.pop(), stack.pop()
                if token == '+':
                    result = int(num_1) + int(num_2)
                elif token == '-':
                    result = int(num_1) - int(num_2)
                elif token == '*':
                    result = int(num_1) * int(num_2)
                elif token == '/':
                    result = int(num_1) / int(num_2)
                else:
                    return
                
                stack.append(result)
            
        return int(stack.pop())
        