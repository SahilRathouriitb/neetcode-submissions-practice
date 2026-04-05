class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s2 = []
        

        while len(asteroids) != 0:

            if len(s2) == 0:
                k = asteroids.pop()
                s2.append(k)

                if len(asteroids) == 0:
                    break

            if (asteroids[-1] > 0) and (s2[-1]>0):
                k = asteroids.pop()
                s2.append(k)
            
            elif (asteroids[-1]<0) and (s2[-1]<0):
                k = asteroids.pop()
                s2.append(k)
            
            else:
                k1 = asteroids.pop()
                k2 = s2.pop()
                if k1<0 and k2>0:
                    s2.append(k2)
                    s2.append(k1)

                elif k1>0 and k2<0:
                    if abs(k1)>abs(k2):
                        asteroids.append(k1)
                    elif abs(k1)<abs(k2):
                        s2.append(k2)
            
        s2.reverse()
        return s2

