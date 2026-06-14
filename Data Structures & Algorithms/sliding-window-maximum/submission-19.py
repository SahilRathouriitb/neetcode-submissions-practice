class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        store = deque([])
        left = 0 
        right = k-1
        output = []

        for i in range(left, right+1):
            if len(store) == 0:
                store.append(nums[i])

            elif nums[i] <= store[-1]:
                store.append(nums[i])

            elif nums[i] > store[-1]:
                while nums[i] > store[-1]:
                    store.pop()
                    if len(store) == 0:
                        break
                store.append(nums[i])                
        output.append(store[0])
        if nums[left] == store[0]:
            store.popleft()

        left += 1
        right += 1
        
        while right < len(nums):
            
            if len(store) == 0 or nums[right] <= store[-1]:
                store.append(nums[right])

            elif nums[right] > store[-1]:
                while nums[right] > store[-1]:
                    store.pop()
                    if len(store) == 0:
                        break
                store.append(nums[right])
            
            output.append(store[0])
            if nums[left] == store[0]:
                store.popleft()
            left += 1
            right += 1
        return output