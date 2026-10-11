class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet = []

        for pos, speed in cars:
            time = (target - pos)/speed
            fleet.append(time)

            while len(fleet)>=2 and fleet[-1]<=fleet[-2]:
                fleet.pop()
        
        return len(fleet)

        