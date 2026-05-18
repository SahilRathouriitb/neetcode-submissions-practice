class Solution:
    def simplifyPath(self, path: str) -> str:
        stack1 = path.split('/')
        stack2 = []

        for i in stack1:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(i)

        if len(stack2) >0:
            return '/'+ "/".join(stack2)
        else:
            return '/'