class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # so nearest car to target is processed first
        cars = sorted(zip(position, speed), reverse= True)

        #fleet starters are placed here
        stack = []

        for pos, spd in cars:
            time = (target-pos)/spd
            stack.append(time)

            #if new time is less than slowest time the both cars belong in the same fleet so no need to add its time
            while len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)

        