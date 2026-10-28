class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        temp = []
        sum = 0
        i = 0
        self.work(nums,temp, output,sum,i,target)
        return output

    def work(self,nums, temp, output, sum, i, target):

        if sum > target:
            return -1
        

        if sum == target:
            output.append(temp.copy())
            return -1
        

        for j in range(i, len(nums)):
            temp.append(nums[j])
            a = self.work(nums, temp, output, sum + nums[j], j, target)
            temp.pop()
            if a == -1:
                break

        return 1 



        
