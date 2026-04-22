class Solution:
 def validPalindrome(self, s: str) -> bool:

        left = 0 
        right = len(s) - 1
        mistake = 0

        while left < right:

            if (s[left] != s[right]) and mistake == 0:

                if (s[right-1] == s[left]) and (s[left+1] != s[right]):
                    right = right - 1    

                elif (s[left+1] == s[right]) and (s[right-1] != s[left]):
                    left = left + 1

                elif (s[left+1] == s[right]) and (s[right-1] == s[left]):
                     
                     if (s[left+1] == s[right-2]):
                          right = right - 1
                     
                     elif (s[right - 1] == s[left +2]):
                          left = left + 1
                     

                else:
                    return False
                    
                mistake = 1
                
            elif (s[left] != s[right]) and (mistake == 1):
                return False

            left += 1
            right -= 1

        return True 


        