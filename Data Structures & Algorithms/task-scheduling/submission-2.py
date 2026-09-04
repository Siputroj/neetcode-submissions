class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max freq in task * n + extra number of char with same freq

        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = [(-1 * freq, task) for task, freq in freq.items()]
        heapq.heapify(heap)

        count = 0

        final_freq = heap[0][0]

        while heap and heapq.heappop(heap)[0] == final_freq:
            count += 1

        final_freq = final_freq * -1 
        return max((final_freq - 1)* (n + 1) + (count), len(tasks))

