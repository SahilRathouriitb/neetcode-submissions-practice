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
                    boat_count += 1
                    
                elif pair > 0:
                    while pair>0:
                        if (pair in dic) and (dic[pair]>0):
                            boat_count += 1
                            dic[pair] = dic[pair] - 1
                            break
                        pair = pair - 1
                        if pair == 0:
                            boat_count += 1
                            
        return boat_count


            
        