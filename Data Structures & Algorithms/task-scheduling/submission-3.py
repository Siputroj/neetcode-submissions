class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())
        max_count = sum(1 for f in freq.values() if f == max_freq)

        result = (max_freq - 1) * (n + 1) + max_count
        return max(result, len(tasks))