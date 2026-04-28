class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        dic = {}
        boat_count = 0

        for i in people:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        
        for i in range(len(people)):
            
            if dic[people[i]] != 0:
                dic[people[i]] = dic[people[i]] - 1
                pair = limit - people[i]

                if pair == 0:
                    boat_count = boat_count + dic[people[i]] + 1
                    dic[people[i]] = 0
                    
                else:
                    j = [i for i in dic if i<= pair and dic[i]>0]
                    if len(j) == 0:
                        # no pair
                        boat_count += 1
                    else:
                        k = max(j)
                        boat_count += 1
                        dic[k] -= 1
                   
        return boat_count


            
        