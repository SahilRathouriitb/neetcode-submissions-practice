class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dict = {}
        # this dict will have position as keys
        # the value will be the corresponding speed

        for i in range(len(position)):
            dict[position[i]] = speed[i]

        # Now we need to sort the position list, so that we know which car is where
        position.sort()

        # now we will create a stack and we will save the position, the topmost cat
        # of the stack wil be the closest to the target

        s = []
        for i in position:
            s.append(i)

        """Now we will one by one pop the elements of the stack"""
        time_array = []
        k = 1
        top = s.pop()
        old_time = (target - top )/dict[top]
        time_array.append(old_time)
        for i in range(1,len(position)):
            a = s.pop()
            new_time = (target-a)/dict[a]
            time_array.append(new_time)
            if new_time> old_time:
                 k = k+1
            old_time = max(new_time,old_time)


        return k
