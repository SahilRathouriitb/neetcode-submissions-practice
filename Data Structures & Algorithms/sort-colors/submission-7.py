class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i = 0
        
        if 0 in dic:
                while dic[0] > 0:
                    nums[i] = 0
                    dic[0] -= 1
                    i += 1
        if 1 in dic:
                while dic[1] > 0:
                    nums[i] = 1
                    dic[1] -= 1
                    i += 1
        if 2 in dic:
            while dic[2] > 0:
                nums[i] = 2
                dic[2] -= 1
                i += 1
