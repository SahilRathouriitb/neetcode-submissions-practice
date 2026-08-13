class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.tracker = 0

    def min_heap(self):
        interior_index = (self.k//2) - 1
        while interior_index >= 0:
            self.heapify_down(interior_index)
            interior_index -= 1
        
        for i in range(self.k, len(self.nums)):
            if self.nums[i] > self.nums[0]:
                self.nums[0] = self.nums[i]
                self.heapify_down(0)
        
        
    
    def heapify_down(self, interior_index):
        # This is heapify down for a min heap
        while True:
            left_index = 2*interior_index + 1
            right_index = 2*interior_index + 2

            l = interior_index
            upper_limit = self.k - 1

            if left_index > upper_limit and right_index > upper_limit:
                break
            if left_index <= upper_limit and self.nums[left_index] < self.nums[l]:
                l = left_index
            if right_index <= upper_limit and self.nums[right_index] < self.nums[l]:
                l = right_index

            if l == interior_index:
                break
            
            self.nums[interior_index], self.nums[l] = self.nums[l], self.nums[interior_index]
            interior_index = l

        
    def add(self, val: int) -> int:

        if len(self.nums) < self.k:
            self.nums.append(val)
            if len(self.nums) == self.k:
                self.min_heap()
                self.tracker = 1
                return self.nums[0]


        elif len(self.nums) >= self.k:
            if self.tracker == 0:
                self.min_heap()
                self.tracker = 1

            if val > self.nums[0]:
                self.nums[0] = val
                self.heapify_down(0)
        
            return self.nums[0]
        
        
        
