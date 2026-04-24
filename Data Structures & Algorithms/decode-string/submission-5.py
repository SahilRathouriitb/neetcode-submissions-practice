class Solution:

 def __init__(self):
    self.l = []   
 
 def decodeString(self,s: str) -> str:
        index = 0
        bracket_count = 0

        while index < len(s):
            if s[index] in [str(i) for i in range(1,10)]:
                num = int(s[index])
                k = 0
                while k<=2: 
                    if s[index + 1] in [str(i) for i in range(0,10)]:
                        index = index + 1
                        num = (num * 10) + int(s[index])
                    k = k + 1
                index = index + 2
                start_index = index
                while True:
                    if s[index] == '[':
                        bracket_count += 1

                    elif (s[index] == ']') and bracket_count != 0:
                        bracket_count -= 1
                    
                    elif (s[index] == ']') and bracket_count == 0:
                        break

                    index = index + 1    

                end_index = index - 1
                self.correct(start_index,end_index,s,num)
                index = index + 1

            else:
                print(s[index])
                self.l.append(s[index])
                index += 1

        return "".join(self.l)


 def correct(self,start_index, end_index,s,num):
    a = s[start_index:end_index+1]*num

    if '[' in a:
        self.decodeString(a)
    else:
        for i in a:
            print(i)
            self.l.append(i)
         


                        
                    
                   

        

        