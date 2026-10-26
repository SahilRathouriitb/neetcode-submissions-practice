from functools import reduce
from operator import xor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Technically i need to find out all the subsets of a given set
        temp = []
        xor_output = []
        self.all_subsets(nums, temp, xor_output, 0)
        return sum(xor_output)

    def all_subsets(self, nums, temp, xor_output, i):

        if i == len(nums):
            result = reduce(xor, temp, 0)
            xor_output.append(result)
            return
        
        self.all_subsets(nums, temp, xor_output, i+1)

        temp.append(nums[i])
        self.all_subsets(nums,temp, xor_output, i+1)
        temp.pop()
        
