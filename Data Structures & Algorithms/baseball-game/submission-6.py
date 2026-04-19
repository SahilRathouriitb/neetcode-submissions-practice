class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0

        for i in (operations):

         
            try:
                    record.append(int(i))
                    sum += int(i)
            except:

                if i == '+':
                    sum = sum + (record[-1]+record[-2])
                    record.append(record[-1]+record[-2])
                    

                elif i == 'D':
                    sum += 2*record[-1]
                    record.append(2*record[-1])
                    

                elif i == 'C':
                    k = record.pop()
                    sum -= k 
            
        
        return sum
                


        