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
            print(min_cap, max_cap)
            mid = min_cap + (max_cap - min_cap)//2
            print("mid", mid)
            if (min_cap == max_cap) or (mid == lower) or (mid == upper):
                return mid
            
            i = 0
            sum = 0
            width = 0
            max_width = 0 
            ships = 0

            while i < len(weights):

                sum = sum + weights[i]

                if sum <= mid:
                    width += 1
                    i += 1
                    if i == len(weights):
                        ships += 1

                elif sum > mid:
                    width = 0 
                    sum = 0 
                    ships += 1
                max_width = max(max_width, width)
            print(ships, max_width)

            if (ships < days) :
                max_cap = mid 
            
            elif ships == days:
                max_cap = mid


            elif (ships > days):
                min_cap = mid + 1
            