from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # step 1 - count the frequency
        dic = {}
        for i in tasks:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        hp = list(dic.values())
        hp.sort(reverse = True)

        time = 0 
        q = deque([])

        while len(hp) > 0 or len(q) > 0:

            time += 1
            # When there are two elements in the heap
            if len(hp) > 1:
                temp = hp[0]
                if temp > 1:
                    q.append((temp-1, time + n))
                move = hp.pop()
                hp[0] = move
                self.heapify_down(hp, 0)
            
            elif len(hp) == 1:
                temp = hp.pop()
                if temp > 1:
                    q.append((temp-1, time + n))
            
            # Now we will look into queue
            if len(q) > 0:
                if time == q[0][1]:
                    qv = q.popleft()
                    hp.append(qv[0])
                    self.max_heap(hp)
        return time



    def max_heap(self, array):
        interior_index = len(array)//2 -1 
        while interior_index >= 0:
            self.heapify_down(array, interior_index)
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
            
            arr[k], arr[index] = arr[index], arr[k]
            index = k 


        