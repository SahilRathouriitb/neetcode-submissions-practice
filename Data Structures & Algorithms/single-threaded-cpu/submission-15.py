class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        output = []
        transition = []
        time = 0

        for i in range(len(tasks)):
            tasks[i].append(i)
        
        # Now i need to make a min heap of this array on the basis of 0th 
        self.min_heap(tasks, 0)
        
        # Now we should start the variable timer with the first task
        time = tasks[0][0]
        time += tasks[0][1]
        output.append(tasks[0][2])
        b = tasks.pop()
        tasks[0] = b
        self.heapify_down(tasks, 0, 0)

        while len(tasks)> 0 or len(transition)>0:
                    if len(tasks) > 0:
                        while time >= tasks[0][0]:
                            transition.append(tasks[0])
                            b = tasks.pop()
                            if len(tasks) > 0:
                                tasks[0] = b
                                self.heapify_down(tasks, 0, 0)
                            else:
                                break
                    self.min_heap(transition, 1)
                    
                    if len(transition)>0:
                        output.append(transition[0][2])
                        time = time + transition[0][1]
                        b = transition.pop()
                        if len(transition) > 0:
                            transition[0] = b
                            self.heapify_down(transition, 0, 1)

                    time += 1
            
            
            
        
        return output
        

    
    def min_heap(self, arr, number):
        if len(arr) == 1:
            return
        interior_index = len(arr)//2 - 1
        while interior_index >= 0:
            self.heapify_down(arr, interior_index, number)
            interior_index -= 1

    
    def heapify_down(self, arr, index, number):
        limit = len(arr) -1 

        while True:
            left = 2*index + 1
            right = 2*index + 2 

            k = index 

            if left > limit and right > limit:
                break

            if left <= limit and arr[left][number] < arr[k][number]:
                k = left
            if right <= limit and arr[right][number] < arr[k][number]:
                k = right
            if number == 0 and left <= limit and arr[left][number] == arr[k][number]:
                if arr[left][1] < arr[k][1]:
                    k = left
            if number == 0 and right <= limit and arr[right][number] == arr[k][number]:
                            if arr[right][1] < arr[k][1]:
                                k = right


            if k == index:
                break
            
            arr[k], arr[index] = arr[index], arr[k]
            index = k 

        



        