class Solution:
 def validPalindrome(self, s: str) -> bool:

        left = 0 
        right = len(s) - 1
        mistake = 0
        conclusion = None

        while left < right:

            if (s[left]) == (s[right]):
                left += 1
                right -= 1

            elif (s[left] != s[right]) and mistake == 0:
                left = left + 1
                mistake = 1
                
            elif (s[left] != s[right]) and (mistake == 1):
                conclusion = False
                break


            if left >= right:
                 return True


        if conclusion == False:
            left = 0 
            right = len(s) - 1
            mistake = 0

            while left < right:

                if (s[left]) == (s[right]):
                    left += 1
                    right -= 1

                elif (s[left] != s[right]) and mistake == 0:
                    right = right - 1
                    mistake = 1
                    
                elif (s[left] != s[right]) and (mistake == 1):
                    return False


                if left >= right:
                    return True

        return True
             




        