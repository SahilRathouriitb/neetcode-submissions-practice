class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.min_heap(nums, k)
        return nums[0]

    def min_heap(self, arr, k):
        interior_index = k//2 - 1
        while interior_index >= 0:
            self.heapify_down(arr, interior_index, k)
            interior_index -= 1
        for i in range(k, len(arr)):
            if arr[i] > arr[0]:
                arr[0] = arr[i]
                self.heapify_down(arr, 0, k)


    def heapify_down(self, arr, index, k):
        upper_limit = k - 1
        while True:
            left = 2*index + 1
            right = 2*index + 2

            r = index

            if left > upper_limit and right > upper_limit:
                break
            if left <= upper_limit and arr[left] < arr[r]:
                r = left
            if right <= upper_limit and arr[right] < arr[r]:
                r = right

            if r == index:
                break
            arr[r], arr[index] = arr[index], arr[r]
            index = r
        

        