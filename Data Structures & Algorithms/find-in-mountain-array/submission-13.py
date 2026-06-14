class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Firstly i need to find the peak 
        ln = mountainArr.length()
        left = 1
        right = ln - 2

        peak_index = None

        while left <= right:
            mid = left + (right - left)//2

            mid_val = mountainArr.get(mid)
            mid_val_prev = mountainArr.get(mid-1)
            mid_val_next = mountainArr.get(mid + 1)

            if (mid_val_prev < mid_val) and (mid_val > mid_val_next):
                peak_index = mid
                break

            elif mid_val < mid_val_next:
                left = mid + 1
            
            elif mid_val_prev > mid_val:
                right = mid - 1
        
        # Now we have the peak index
        # We will firstly perform binary search on the first half

        left = 0 
        right = peak_index

        while left <= right:
            mid = left + (right-left)//2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid

            elif mid_val < target:
                left = mid + 1
            
            elif mid_val > target:
                right = mid - 1

        # Say the left search didnt get anything
        # Now we will perform the right search

        left = peak_index + 1
        right = ln - 1

        while left <= right:
            mid = left + (right - left)//2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid
            
            elif mid_val > target:
                left = mid + 1
            
            elif mid_val < target:
                right = mid - 1

        return -1
            

            




        