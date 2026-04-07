class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        record = {0}
        tracker_list_sum = 0
        
        tracker_list_sum += nums[right]
        counter = 1
        

        while True:
            
            if tracker_list_sum < target:
                right = right + 1
                if right == len(nums):
                    break
                tracker_list_sum += nums[right] 
                counter = counter + 1

            elif tracker_list_sum >= target:
                record.add(counter)
                tracker_list_sum = tracker_list_sum - nums[left]
                counter = counter - 1
                left = left + 1
                

        if len(record) != 1:
            record.remove(0)
            return min(record)
        
        else:
            return 0


        