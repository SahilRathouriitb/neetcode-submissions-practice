class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        for i in range(len(temperatures)):
            j = i+1
            k = 1

            if j<= (len(temperatures)-1):
                while temperatures[i]>=temperatures[j]:
                    k = k+1
                    j = j + 1
                    if (j>len(temperatures)-1):
                        k = 0
                        break
            else:
                 k = 0
            l.append(k)
            
        return l