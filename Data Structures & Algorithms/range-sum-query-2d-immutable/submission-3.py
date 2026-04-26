class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_mat = self.prefix_matrix(self.matrix)

    def prefix_matrix(self, matrix):
        trow = len(matrix)
        tcol = len(matrix[0])
    
        # Construction of prefix matrix
        pre_mat = []
        for i in range(trow):
            pre_mat.append([]) 
            for j in range(tcol):
                pre_mat[i].append(None)
                

        sum = 0
        for i in range(trow):
            sum = sum + matrix[i][0]
            pre_mat[i][0] = sum
        

        sum = 0 
        for i in range(tcol):
            sum = sum + matrix[0][i]
            if i>0:
                pre_mat[0][i] = sum


        for i in range(1,tcol):
            for j in range(1,trow):
                total = matrix[j][i] + pre_mat[j][i-1] + pre_mat[j-1][i] - pre_mat[j-1][i-1]
                pre_mat[j][i] = total
        
        return pre_mat

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_mat[row2][col2]
        if (row1-1)>=0:
            upper_total = self.prefix_mat[row1-1][col2]
        else:
            upper_total = 0

        if (col1-1)>=0:
            left_total = self.prefix_mat[row2][col1-1]
        else:
            left_total = 0

        if (row1-1)>=0 and (col1-1)>=0:
            common_total = self.prefix_mat[row1-1][col1-1]
        else:
            common_total = 0

        return total - upper_total - left_total + common_total

