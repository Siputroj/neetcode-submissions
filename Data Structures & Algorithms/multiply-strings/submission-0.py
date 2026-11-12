class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        table = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

        order = 1
        first = 0
        for i in range(len(num1) -1, -1 , -1):
            first += (table[num1[i]] * order)
            order *= 10

        order = 1
        second = 0
        for i in range(len(num2) -1, -1 , -1):
            second += (table[num2[i]] * order)
            order *= 10

        return str(first * second)