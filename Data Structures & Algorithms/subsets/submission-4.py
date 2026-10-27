class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        temp = []
        flag = True
        self.iter(nums, output, temp, flag, i = 0)
        return output

    def iter(self, nums, output, temp, flag, i):
        if len(nums) == i:
            output.append(temp.copy())
            return

        self.iter(nums, output, temp, False, i+1)

        if flag == False and nums[i] == nums[i-1]:
            return

        temp.append(nums[i])
        self.iter(nums, output, temp, True, i+1)
        temp.pop()

        
        