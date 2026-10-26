from functools import reduce
from operator import xor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Technically i need to find out all the subsets of a given set
        temp = []
        output = [0]
        self.all_subsets(nums, temp, output, 0, xor = 0)
        return output[0]

    def all_subsets(self, nums, temp, output, i, xor):

        if i == len(nums):
            output[0] += xor
            return xor
        
        self.all_subsets(nums, temp, output, i+1, xor)

        temp.append(nums[i])
        xor = xor ^ nums[i]
        self.all_subsets(nums,temp, output, i+1, xor)
        temp.pop()
        
