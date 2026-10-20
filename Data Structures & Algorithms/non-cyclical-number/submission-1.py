class Solution:
    def isHappy(self, n: int) -> bool:
        numset = set()

        while n not in numset:
            numset.add(n)
            total = 0
            for d in str(n):
                d = int(d)
                total += (d * d)
            
            if total == 1:
                return True
            n = total

        return False

        