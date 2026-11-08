class Solution:

    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_sides = sum(matchsticks)

        if sum_sides % 4 != 0:
            return False
        
        side_length = sum_sides/4

        for i in matchsticks:
            if i > sum_sides:
                return False
        sides = [0,0,0,0]
        matchsticks.sort(reverse = True)
        return self.check(matchsticks, sides, side_length, i = 0) 

    
    def check(self, matchsticks, sides, side_length, i):
        if i == len(matchsticks):
            return True
        
        for j in range(4):
            if sides[j] + matchsticks[i] <= side_length:
                sides[j] += matchsticks[i]
                val = self.check(matchsticks, sides, side_length, i+1)
                if val:
                    return True
                sides[j] -= matchsticks[i]
        
        return False

        


       