class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        s = []
        for i in tokens:
            if i in {'+','-','*','/'}: 
                a = s.pop()
                b = s.pop()
                if i == '+':
                    s.append(b+a)
                elif i == '-':
                    s.append(b-a)
                elif i == '*':
                    s.append(b*a)
                elif i == '/':
                    s.append(int(b/a))
                print(s)
            else:
                 s.append(int(i))
        
        return s[-1]