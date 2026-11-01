class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        temp = []
        sum = 0
        i = 0
        flag = True
        
        self.check(output, temp, sum, i, target, candidates, flag)
        return output

    def check(self, output, temp, sum, i , target, nums, flag):
        if sum == target:
            output.append(temp.copy())
            return 
        if i == len(nums) or sum > target:
            return 

        self.check(output, temp, sum, i +1, target, nums, flag = False)

        if flag == False and nums[i] == nums[i-1]:
            return 
        temp.append(nums[i])
        self.check(output, temp, sum + nums[i], i+1, target, nums, flag = True)
        temp.pop()
    
    
