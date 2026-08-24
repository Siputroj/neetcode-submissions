class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # table of key: list pair, where list contains tuples of timestamps and value
        if key not in self.table:
            self.table[key] = []
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""

        arr = self.table.get(key)

        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = left + (right - left) // 2

            if timestamp >= arr[mid][0]:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res
