class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left<=right:

            mid = left + (right-left)//2

            if (matrix[mid][0]) <= target <= (matrix[mid][len(matrix[mid])-1]):
                return self.binary_search(matrix[mid], target)
            
            elif target < matrix[mid][0]:
                if mid > 0:
                    right = mid - 1
                else:
                    return False
                
            elif target > matrix[mid][len(matrix[mid])-1]:
                if mid < (len(matrix)-1):
                    left = mid + 1
                else: 
                    return False
                
        return False


            

    def binary_search(self, array, target):
        
            left = 0 
            right = len(array) - 1

            while left <= right:

                mid = left + (right - left)//2

                if target == array[mid]:
                    return True
                
                elif target > array[mid]:
                    left = mid + 1

                elif target < array[mid]:
                    right = mid - 1
                    
            return False
        
