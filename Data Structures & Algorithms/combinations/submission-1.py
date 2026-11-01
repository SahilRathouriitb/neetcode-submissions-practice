class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        temp = []
        output = []
        i = 0
        self.check(nums, temp, output, i, k)
        return output

    def check(self, nums, temp, output, i, k):
        if len(temp) == k:
            output.append(temp.copy())
            return 
        
        if i == len(nums):
            return 
        
        self.check(nums, temp, output, i+1, k)

        temp.append(nums[i])
        self.check(nums, temp, output, i+1, k)
        temp.pop()

        