class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for number in range(n + 1):
            temp = 0

            while number:
                temp += number & 1
                number >>= 1

            res.append(temp)
        return res