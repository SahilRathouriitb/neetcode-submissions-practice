from functools import reduce
from operator import xor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Technically i need to find out all the subsets of a given set
        temp = []
        output = [0]
        self.all_subsets(nums, temp, output, 0)
        return output[0]

    def all_subsets(self, nums, temp, output, i):

        if i == len(nums):
            result = reduce(xor, temp, 0)
            output[0] += result
            return
        
        self.all_subsets(nums, temp, output, i+1)

        temp.append(nums[i])
        self.all_subsets(nums,temp, output, i+1)
        temp.pop()
        
