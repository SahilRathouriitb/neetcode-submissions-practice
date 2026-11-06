class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        output = []
        dic = {'(':n, ')':n}
        open_count = 0
        self.check(temp, output, dic, open_count, n)
        return output
    
    def check(self, temp, output, dic, open_count, n):
        if len(temp) == 2*n:
            output.append("".join(temp))
            return 

        for i in dic:
            if i == ')' and open_count == 0:
                continue
            
            if i == '(' and dic[i] != 0:
                temp.append(i)
                dic['('] -= 1
                self.check(temp, output, dic, open_count + 1, n)  
                temp.pop()
                dic['('] += 1

            elif i == ')' and open_count > 0:
                temp.append(')')
                dic[')'] -= 1
                self.check(temp, output, dic, open_count -1, n)
                temp.pop()
                dic[')'] += 1

        