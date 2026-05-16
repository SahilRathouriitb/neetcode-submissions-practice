class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        i = 0
        while arr[i] <= x:
            i += 1
            if i == len(arr):
                break
    
        if (i-k) >= 0:
            lower_index = i - k
            upper_index = i - 1
        else:
            lower_index = 0
            upper_index = k-1

        if upper_index + 1 < len(arr):
            while (x-arr[lower_index]) > (arr[upper_index + 1]-x):
                    lower_index += 1
                    upper_index += 1
                    if upper_index == len(arr)-1:
                        break
            
        return (arr[lower_index:upper_index+1])