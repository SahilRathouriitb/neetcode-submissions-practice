class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        runs = 0
        index = 0
        k = 0

        while runs < len(nums):

            if (index != 0) and (nums[index] == nums[index-1]):
                # this is when we have found a duplicate at nums i
                self.shift(nums, index)

            else:
                k += 1
                index += 1
            
            runs += 1

        #print(nums)
        return k 

    def shift(self,nums, start_index): 
        for i in range(start_index, len(nums)-1):
            nums[i] = nums[i+1]

