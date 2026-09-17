class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors = []
        for a in asteroids:
            destroyed = False

            #while both prev ast. and new ast. are travelling in collision course
            while survivors and survivors[-1]>0 and a<0:

                if survivors[-1]< (a*-1):
                    survivors.pop()
                elif survivors[-1]> (a*-1):
                    destroyed = True
                    break
                elif survivors[-1]==(a*-1):
                    destroyed = True
                    survivors.pop()
                    break
            if not destroyed:
                survivors.append(a)
            
        return survivors

        