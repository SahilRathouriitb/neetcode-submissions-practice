class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict = {}
        
        for i in range(len(position)):
            dict[position[i]] = speed[i]

    
        position.sort()

        s = []
        for i in position:
            s.append(i)

        """Now we will one by one pop the elements of the stack"""
        
        k = 1
        top = s.pop()
        old_time = (target - top )/dict[top]

        for i in range(1,len(position)):
            a = s.pop()
            new_time = (target-a)/dict[a]
            
            if new_time> old_time:
                 k = k+1
            old_time = max(new_time,old_time)


        return k
