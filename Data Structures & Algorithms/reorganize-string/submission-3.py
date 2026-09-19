class Solution:
    def reorganizeString(self, s: str) -> str:
        count_dic = {}
        count_list = []
        output = []

        for i in s:
            if i in count_dic:
                count_dic[i] += 1
            else:
                count_dic[i] = 1

        for i in count_dic:
            count_list.append([i, count_dic[i]])
        # After this we have a frequency counter and i can construct max heap
        self.max_heap(count_list)

        hold = [0,0]

        while len(count_list) > 0:

            top = count_list[0]
            output.append(top[0])
            top[1] -= 1

            if hold[1] > 0:
                count_list[0] = hold    
            else:
                temp = count_list.pop()
                if len(count_list) > 0:
                    count_list[0] = temp
                else:
                    break
            
            self.heapify_down(count_list, 0)
            hold = top
        a = "".join(output)
        if len(a) == len(s):
            return a 
        else:
            return "" 
           

            


    
    def max_heap(self, arr):
        int_node = len(arr)//2 - 1

        while int_node >= 0:
            self.heapify_down(arr, int_node)
            int_node -= 1
    
    def heapify_down(self, arr, index):
        limit = len(arr) -1 

        while True:
            left = 2*index + 1
            right = 2*index + 2

            k = index

            if left > limit and right > limit:
                break

            if left <= limit and arr[left][1] > arr[k][1]:
                k = left
            if right <= limit and arr[right][1] > arr[k][1]:
                k = right

            if k == index:
                break

            arr[k],arr[index] = arr[index], arr[k]
            index = k 
            


