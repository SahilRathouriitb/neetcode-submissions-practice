import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        while k > 0:
            max_index = 0 
            max_value = 0
            for i in range(len(gifts)):
                if gifts[i] > max_value:
                    max_value = gifts[i]
                    max_index = i
            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))
            k -= 1
        
        return sum(gifts)
