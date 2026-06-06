class Solution:
    def minWindow(self, s: str, t: str) -> str:

        temp_check = {}
        store = None
        
        for i in t:
                if i in temp_check:
                    temp_check[i] = temp_check[i] + 1
                else:
                    temp_check[i] = 1
            

        i = 0
        while i < len(s):
            
            

            if s[i] in temp_check:
                left = i
                
                temp_check[s[i]] = temp_check[s[i]] - 1
                if temp_check[s[i]] == 0:
                    temp_check.pop(s[i])
                
                if len(temp_check) == 0:
                    right = left
                    if store == None:
                            store = [left,right, right-left]
                    elif (right-left < store[2]):
                            store = [left,right, right-left]
        

                right = i + 1
                while (right < len(s)) and (len(temp_check)>0):
    
                    if s[right] in temp_check:
                        temp_check[s[right]] = temp_check[s[right]] - 1
                        if temp_check[s[right]] == 0:
                            temp_check.pop(s[right])

                        if len(temp_check) == 0:
                            if store == None:
                                store = [left,right, right-left]
                            elif (right-left < store[2]):
                                store = [left,right, right-left]
                            break

                    right += 1
                
                for j in t:
                    if j in temp_check:
                        temp_check[j] = temp_check[j] + 1
                    else:
                        temp_check[j] = 1

            
            i += 1
        
        if store == None:
            return ""
        else:

            return s[store[0]:store[1]+1]
                
        
        