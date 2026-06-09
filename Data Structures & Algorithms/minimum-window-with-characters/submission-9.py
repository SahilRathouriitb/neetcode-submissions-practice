class Solution:
    def minWindow(self, s: str, t: str) -> str:
        og = {}
        
        for i in t:
            if i in og:
                og[i] += 1
            else:
                og[i] = 1
        
        #print(og)

        store = None
        temp = {}
        temp_have = 0

        left = 0 
        right = 0


        while (right < len(s)) and (left < len(s)):

            while temp_have < len(og):

                if s[right] in og:

                    if s[right] in temp:
                        temp[s[right]] += 1
                    else:
                        temp[s[right]] = 1

                    if temp[s[right]] == og[s[right]]:
                        temp_have += 1
                        print('ok')

                    

                right += 1
                if right == len(s):
                    break
            
            
            while temp_have == len(og):
                if store == None:
                    store = [left, right, right-left]
                else:
                    if (right - left) < store[2]:
                        store = [left, right, right-left]

                # Now i am about to increment left, so i will remove the left match 
                if s[left] in temp:
                    temp[s[left]] -= 1
                    if temp[s[left]] < og[s[left]]:
                        temp_have -= 1

                left += 1
            
        #print(store)
        if store == None:
            return ""
        else:
            return s[store[0]:store[1]]

            
        

