class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        store = deque([nums[0]])
        left = 0 
        right = k-1
        output = []

        for i in range(left+1, right+1):

            if nums[i] <= store[-1]:
                store.append(nums[i])

            elif nums[i] > store[-1]:
                while (len(store) > 0) and (nums[i] > store[-1]):
                    store.pop()
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
                while len(store) > 0 and nums[right] > store[-1]:
                    store.pop()
                store.append(nums[right])
            
            output.append(store[0])
            if nums[left] == store[0]:
                store.popleft()
            left += 1
            right += 1
        return output