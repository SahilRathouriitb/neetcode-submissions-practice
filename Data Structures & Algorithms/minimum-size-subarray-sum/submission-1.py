class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        record = {0}
        tracker_list = []
        tracker_list_sum = 0

        tracker_list.append(nums[right])
        tracker_list_sum += nums[right]

        while True:

            if tracker_list_sum < target:
                right = right + 1
                if right == len(nums):
                    break
                tracker_list.append(nums[right])
                tracker_list_sum += nums[right] 

            elif tracker_list_sum >= target:
                record.add(len(tracker_list))
                left = left + 1
                tracker_list_sum = tracker_list_sum - tracker_list[0]
                tracker_list.pop(0)

        if len(record) != 1:
            record.remove(0)
            return min(record)
        
        else:
            return 0


            



        