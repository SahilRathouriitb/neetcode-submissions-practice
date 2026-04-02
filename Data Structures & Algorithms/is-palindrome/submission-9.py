class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
        i = 0
        j = len(s)-1
        while (i <j):
            
            if s[i].lower() not in chars:
                i = i+1
            if s[j].lower() not in chars:
                j = j-1
            if (s[i].lower() in chars) and (s[j].lower() in chars): 
                if s[i].lower() != s[j].lower():
                    return False 
                else:
                    i = i+1
                    j = j-1
                    
        return True
                


        