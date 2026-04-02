class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
             return strs[0]
        
        counter = 0 
        letter_number = 0
        text = ""
        return_val = ""
        
        while letter_number <= len(strs[counter])-1:

                if len(text)>0:
                    if (strs[counter][letter_number]) != text:
                            break
                else:
                    text = strs[counter][letter_number]

                counter = counter + 1

                if counter == len(strs):
                    return_val = return_val + text
                    text = ""
                    counter = 0 
                    letter_number = letter_number + 1

        return return_val
        
      


                