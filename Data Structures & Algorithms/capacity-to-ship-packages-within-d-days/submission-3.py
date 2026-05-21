class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = 0
        for i in weights:
            max_cap += i

        # we need to find out the suitable value in between min_cap and max_cap using binary search
        lower = min_cap
        upper = max_cap

        while True:
            mid = min_cap + (max_cap - min_cap)//2
            if (min_cap == max_cap) or (mid == lower) or (mid == upper):
                return mid
            
            i = 0
            sum = 0
            ships = 0

            while i < len(weights):

                sum = sum + weights[i]

                if sum <= mid:
                    i += 1
                    if i == len(weights):
                        ships += 1

                elif sum > mid:
                    sum = 0 
                    ships += 1
                

            if (ships < days) :
                max_cap = mid 
            
            elif ships == days:
                max_cap = mid


            elif (ships > days):
                min_cap = mid + 1
            