class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total/4
        for i in matchsticks:
            if i> side:
                return False

        output = []
        s = 0
        l= 0
        self.check(side, matchsticks, s , output, l)
        print(output)
        print(matchsticks)
        if len(output) >= 4:
            return True
        else:
            return False

    def check(self, side, match, s, output, l):

        if s == side:
            output.append(1)
            return 'T'
        elif s > side:
            return 'F'

        for k in range(len(match)):
            if match[k] < 0:
                continue
            
            match[k] = -match[k]
            print(match[k])
            val = self.check(side, match, s-match[k], output, l+1)
            if val == 'F':
                match[k] = -match[k]
                return 1
            if val == 1:
                match[k] = -match[k]
            



        