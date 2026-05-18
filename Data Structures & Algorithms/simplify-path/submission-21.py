class Solution:
    def simplifyPath(self, path: str) -> str:
        stack1 = path.split('/')
        print(stack1)
        stack2 = ['']
        print(stack2)

        for i in stack1:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if (len(stack2) > 0):
                    if len(stack2) == 1 and stack2[0] == '':
                        continue
                    else:
                        stack2.pop()
            else:
                stack2.append(i)
        print(stack2)
        if len(stack2) >0:
            if len(stack2) == 1 and stack2[0] == '':
                return '/'
            return "/".join(stack2)
        else:
            return '/'