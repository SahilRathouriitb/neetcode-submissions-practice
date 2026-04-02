class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # firstly we will count the number of zero's we have in the array
        # if the number of zeros is more than 2, then all zero 
        n = 0
        for i in nums:
            if i == 0:
                n = n+1
            if n>1:
                break
        if n<=1:
            # Here i am assuming that at max only one element is 0 in the list
            a = 1
            b = 1
            for i in range(len(nums)):
                a = nums[i]*a
                if nums[i] != 0:
                    b = b*nums[i]

            
            l = []
            for i in range(len(nums)):

                if a == 0 and nums[i]!=0:
                    l.append(0)
                elif a == 0 and nums[i] == 0:
                    l.append(int(b))
                elif a!=0:
                    l.append(int((a/nums[i])))
            
            return l
        else:
            return [0]*len(nums)


       
