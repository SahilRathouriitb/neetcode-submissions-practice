class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left<right:

            if people[left] + people[right] <= limit:
                boats += 1
                left = left + 1
                right = right - 1

            else:

                if people[right] <= limit:
                    boats += 1
                    right = right - 1

        if left == right:
            boats += 1        

        return boats
                 


            
        