class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        tracker_list_sum = 0
        
        tracker_list_sum += nums[right]
        counter = 1
        k = 2*len(nums)

        while True:
            
            if tracker_list_sum < target:
                right = right + 1
                if right == len(nums):
                    break
                tracker_list_sum += nums[right] 
                counter = counter + 1

            elif tracker_list_sum >= target:
                k = min(counter,k)
                tracker_list_sum = tracker_list_sum - nums[left]
                counter = counter - 1
                left = left + 1
                
        
        if k == 2*len(nums):
             return 0 
        else:
            return k


        