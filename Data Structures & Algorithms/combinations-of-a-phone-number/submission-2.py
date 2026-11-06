class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        map = {'2':'abc','3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        temp = []
        output = []
        self.check(temp, output, digits, map, i = 0)
        return output


    def check(self, temp, output, digits, map, i):
        if len(temp) == len(digits):
            output.append("".join(temp))
            return

        
        for j in map[digits[i]]:
            temp.append(j)
            self.check(temp, output, digits, map, i+1)
            temp.pop()


        
