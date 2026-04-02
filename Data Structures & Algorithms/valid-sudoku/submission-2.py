class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       

     # Row checking 
     for i in range(len(board)):
        dict = {}
        for j in board[i]:
          if j != '.':
            if j not in dict:
                dict[j] = 0
            
            dict[j] = dict[j] + 1

        for i in dict:
           if dict[i]>1:
              return False
           

     # Column Checking 
     for i in range(len(board)):
        dict = {}
        for j in range(len(board)):
          if board[j][i] != '.':
            if board[j][i] not in dict:
                dict[board[j][i]] = 0
            
            dict[board[j][i]] = dict[board[j][i]] + 1
        
        for i in dict:
           if dict[i]>1:
              return False
           
    
     # Mini Grid Checking 
     complex_dict = {}
     for i in range(len(board)):
       for j in range(len(board)):
          
          index = (i//3)*3 + (j//3)
          if board[i][j] != '.':
             if index not in complex_dict:
                complex_dict[index] = {}
             if board[i][j] not in complex_dict[index]:
                complex_dict[index][board[i][j]] = 0

             complex_dict[index][board[i][j]] = complex_dict[index][board[i][j]] + 1

     # Now we need to check thing in blocks

     for i in complex_dict:
       for j in complex_dict[i]:
          if complex_dict[i][j]>1:
             return False
          
     return True

        


        

    
