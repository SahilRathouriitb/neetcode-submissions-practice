class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        """ method 1 is sort this and then check the count and the one
            with more than threshold count will be stored in the list 
            If i use heap sort, in that case time will be nlogn and space will be 1
        """

        
        s = {}
        for i in range(len(nums)):
            if nums[i] not in s:
                s[nums[i]] = 1
            else:
                s[nums[i]] = s[nums[i]] + 1
        
        return [i for i in s if s[i] > (len(nums)//3)]
