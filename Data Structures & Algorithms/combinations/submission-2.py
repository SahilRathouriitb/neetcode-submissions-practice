class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        output = []
        i = 1
        self.check(n, temp, output, i, k)
        return output

    def check(self, n, temp, output, i, k):

        if len(temp) == k:
            output.append(temp.copy())
            return 
        
        if i > n:
            return 
        
        for j in range(i, n+1):
            temp.append(j)
            self.check(n, temp, output, j+1, k)
            temp.pop()


        

        