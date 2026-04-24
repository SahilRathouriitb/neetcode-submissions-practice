class Solution:

    def decodeString(self,s: str) -> str:
        stack = []
        i = 0
        

        while i<len(s):

            if s[i] != ']':
                stack.append(s[i])

            elif s[i] == ']':
                store = ''
                # Now we will capture what is inside the bracket 
                while stack[-1] != '[':
                    k = stack.pop()
                    store = k + store
                # This pop will remove the opening bracked
                stack.pop()

                # We need to count the number now 
                num = 0
                j = 1
                while stack[-1] in [str(i) for i in range(0,10)]:
                    digit = stack.pop()
                    num = num + int(digit)*j
                    j = j*10
                    if len(stack) == 0:
                        break
                store = store * num

                for j in store:
                    stack.append(j)
            i = i + 1
        
        return "".join(stack)


            
