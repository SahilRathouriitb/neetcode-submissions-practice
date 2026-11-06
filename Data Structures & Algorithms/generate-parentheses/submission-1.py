class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        output = []
        dic = {'(':n, ')':n}
        self.check(temp, output, dic, n)
        return output
    
    def check(self, temp, output, dic,  n):
        if len(temp) == 2*n:
            output.append("".join(temp))
            return 

        open_count = (n - dic['(']) - (n-dic[')'])
        for i in dic:
            if i == ')' and open_count == 0:
                continue
            
            if i == '(' and dic[i] != 0:
                temp.append(i)
                dic['('] -= 1
                self.check(temp, output, dic, n)  
                temp.pop()
                dic['('] += 1

            elif i == ')' and open_count > 0:
                temp.append(')')
                dic[')'] -= 1
                self.check(temp, output, dic, n)
                temp.pop()
                dic[')'] += 1

        