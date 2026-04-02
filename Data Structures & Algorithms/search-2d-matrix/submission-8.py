class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        return self.Matrix(matrix, target, 0, len(matrix) - 1)


    def Matrix(self, matrix, target, left, right):

        if left > right:
            return False

        mid = left + (right - left)//2
        last = len(matrix[mid]) - 1

        if matrix[mid][0]<= target <= matrix[mid][last]:
            return self.binary_search(matrix[mid], target, 0 , len(matrix[mid]) -1 )

        elif target < matrix[mid][0]:
            if mid > 0:
                right = mid - 1
                return self.Matrix(matrix, target, left, right)
            else:
                return False
            
        
        elif target > matrix[mid][last]:
            if mid < (len(matrix) - 1):
                left = mid + 1
                return self.Matrix(matrix, target, left, right)
            else:
                return False
            
            
        




    def binary_search(self, array, target, left, right):

        try:
            mid = left + (right -left)//2

            if array[mid] == target:
                return True

            elif target< array[mid]:
                right = mid - 1
                return self.binary_search(array,target, left, right)
            
            elif target > array[mid]:
                left = mid + 1
                return self.binary_search(array, target, left, right)

        except:
            return False
        
