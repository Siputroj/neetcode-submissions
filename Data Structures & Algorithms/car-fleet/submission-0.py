class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # distance = s * t
        # car a b overlap if (target - d_a) / speed_a <= (target - d_b) / speed_b

        cars = sorted(zip(position, speed))
        stack = []

        for i in range(len(cars) -1, -1, -1):
            position, speed = cars[i]
            time = (target - position) / speed

            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)

        return len(stack)



        
