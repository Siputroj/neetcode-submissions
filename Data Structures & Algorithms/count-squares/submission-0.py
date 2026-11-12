class CountSquares:

    def __init__(self):
        self.points = dict()
        self.total_points = 0

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.points:
            self.points[tuple(point)] = 1
        else:
            self.points[tuple(point)] += 1
        self.total_points += 1

    def count(self, point: List[int]) -> int:
        x, y = tuple(point)
        if self.total_points < 3:
            return 0
        
        res = 0
        for dist in range(1, 1000 + 1):
            left, top, right, bottom = (x - dist, y), (x, y + dist), (x + dist, y), (x, y - dist)

            # left-top
            if left in self.points and top in self.points:
                # diagonal point
                diagonal = (left[0], left[1] + dist)
                if diagonal in self.points:
                    # count
                    res += (self.points[left] * self.points[top] * self.points[diagonal])

            # left-bottom
            if left in self.points and bottom in self.points:
                # diagonal point
                diagonal = (left[0], left[1] - dist)
                if diagonal in self.points:
                    # count
                    res += (self.points[left] * self.points[bottom] * self.points[diagonal])
            
            # right-top
            if right in self.points and top in self.points:
                # diagonal point
                diagonal = (right[0], right[1] + dist)
                if diagonal in self.points:
                    # count
                    res += (self.points[right] * self.points[top] * self.points[diagonal])
            
            # right-bottom
            if right in self.points and bottom in self.points:
                # diagonal point
                diagonal = (right[0], right[1] - dist)
                if diagonal in self.points:
                    # count
                    res += (self.points[right] * self.points[bottom] * self.points[diagonal])

        return res

