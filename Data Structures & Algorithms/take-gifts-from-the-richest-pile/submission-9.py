import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        self.max_heap(gifts)
        while k > 0:
            gifts[0] = math.floor(math.sqrt(gifts[0]))
            self.heapify_down(gifts, 0)
            k -= 1
        
        return sum(gifts)

    
    def max_heap(self, arr):
        interior_index = len(arr)//2 - 1
        while interior_index >= 0:
            self.heapify_down(arr, interior_index)
            interior_index -= 1

    def heapify_down(self, arr, index):
        limit = len(arr) - 1
        while True:
            left = 2*index + 1
            right = 2*index + 2

            k = index 

            if left > limit and right > limit:
                break
            
            if left <= limit and arr[left] > arr[k]:
                k = left 
            
            if right <= limit and arr[right] > arr[k]:
                k = right

            if k == index:
                break

            arr[index], arr[k] = arr[k], arr[index]
            index = k 
