class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)
        stack = []
        stack.append(cars[0])
        i = 1
        def calcETA(car: List[int]):
            position = car[0]
            speed = car[1]
            return (target - position) / speed
        while i < len(cars):
            if calcETA(cars[i]) <= calcETA(stack[-1]):
                i+=1
                continue
            else:
                stack.append(cars[i])
            i+=1
        return len(stack)

            
            


        