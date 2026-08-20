class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            curr_temp = temperatures[i]

            while stack:
                future_temp, index = stack[-1]
                if future_temp > curr_temp:
                    res.append(index - i)
                    break
                else:
                    stack.pop()
            
            if not stack:
                res.append(0)

            stack.append((temperatures[i], i))

        return res[::-1]