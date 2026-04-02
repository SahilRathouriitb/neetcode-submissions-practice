class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
             return strs[0]
        
        counter = 0 
        letter_number = 0
        lst = []
        return_val = ""
        
        while letter_number <= len(strs[counter])-1:

                if len(lst)>0:
                    if (strs[counter][letter_number]) != (lst[0]):
                            break
                else:
                    lst.append(strs[counter][letter_number])

                counter = counter + 1

                if counter == len(strs):
                    return_val = return_val + lst[0]
                    lst = []
                    counter = 0 
                    letter_number = letter_number + 1

        return return_val
        
      


                