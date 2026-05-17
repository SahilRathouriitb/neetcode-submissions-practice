class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        i = 1
        dot_count = 0
        while i < len(path):

                if (stack[-1] == '/') and (path[i] == '/'):
                    i += 1
                
                elif (path[i] not in ['/','.']):
                    stack.append(path[i])
                    i += 1 
                
                elif (stack[-1] != '/') and (path[i] == '/'):
                    stack.append(path[i])
                    i += 1
                
                elif path[i] == '.' and path[i-1] == '/':
                     
                    while path[i] == '.':
                        dot_count += 1
                        i += 1
                        if i == len(path):
                            break
                    
                    if dot_count > 2:
                        for k in range(dot_count):
                            stack.append('.')
                    
                    elif (dot_count == 1) and (i != len(path)):
                        if path[i] != '/':
                            stack.append('.')

                    elif (dot_count == 2) and (i != len(path)):
                        if path[i] != '/': 
                            stack.append('.')
                            stack.append('.')
                        else:
                            dash_counter = 0
                            while True:
                                if stack[-1] == '/':
                                    dash_counter += 1
                                if dash_counter == 2:
                                    break
                                if dash_counter == 1:
                                    stack.pop()
                                
                                if len(stack) == 0:
                                    stack.append('/')
                                    break

                    else:
                        # popping logic 
                        dash_counter = 0
                        while True:
                            if stack[-1] == '/':
                                dash_counter += 1
                            if dash_counter == 2:
                                break
                            if dash_counter == 1:
                                stack.pop()
                            
                            if len(stack) == 0:
                                stack.append('/')
                                break
                    dot_count = 0
                elif path[i] == '.':
                    stack.append('.')
                    i += 1

        if stack[-1] == '/' and len(stack) != 1:
            stack.pop()
        return "".join(stack)
                
                            