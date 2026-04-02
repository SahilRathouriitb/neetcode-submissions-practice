class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0] 
        fast = nums[0] 
        s = 0

        while True:
            s = slow
            slow = nums[slow]
            fast = nums[nums[fast]]   

            if slow == fast:
                  break
            
        second_slow  = nums[0]
        loop_mover = nums[s]
        while True:
              if second_slow == loop_mover:
                    return second_slow
              second_slow = nums[second_slow]
              loop_mover = nums[loop_mover]
              
