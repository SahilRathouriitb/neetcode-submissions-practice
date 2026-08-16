class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap(stones)

        while len(stones) > 1:

            h1 = stones[0]
            temp = stones.pop()
            stones[0] = temp
            self.heapify_down(stones, 0, len(stones)-1)
            # now after this second highest element is at the top
            h2 = stones[0]

            if h1 != h2:
                diff = abs(h1-h2)
                stones[0] = diff
                self.heapify_down(stones, 0, len(stones)-1)
            
            else:
                last = stones.pop()
                if len(stones) == 0:
                    return 0
                stones[0] = last
                self.heapify_down(stones, 0, len(stones)-1)
        return stones[0]



    def max_heap(self, arr):
        internal_index = len(arr)//2 - 1
        while internal_index >= 0:
            max_index = len(arr)-1
            self.heapify_down(arr, internal_index, max_index)
            internal_index -= 1

    def heapify_down(self, arr, index, max_index):
        while True: 
            left = 2*index + 1
            right = 2*index + 2
            k = index 
            if left > max_index and right > max_index:
                break
            if left <= max_index and arr[left] > arr[k]:
                k = left
            if right <= max_index and arr[right] > arr[k]:
                k = right

            if k == index:
                break
            arr[index], arr[k] = arr[k], arr[index]
            index = k
        