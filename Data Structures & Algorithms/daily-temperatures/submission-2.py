class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []

        for i in range(len(temperatures) -1, -1, -1):
            curr_temp = temperatures[i]

            while stack:
                future_temp, future_index = stack[-1]
                if future_temp > curr_temp:
                    result.append(future_index - i)
                    break
                else:
                    stack.pop()

            if not stack:
                result.append(0)

            stack.append((curr_temp, i))

        return result[::-1]

