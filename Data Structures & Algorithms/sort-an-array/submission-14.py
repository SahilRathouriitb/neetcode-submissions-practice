class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
       
        for i in range(len(nums)):
            temp = 0
            for j in range(0, len(nums)-i-1):

                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    temp = 1
            
            if temp == 0:
                break

        return nums