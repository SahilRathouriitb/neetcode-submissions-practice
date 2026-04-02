class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Let's solve this using prefix and postfix technique

        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i]*prefix[i-1])

        suffix = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            
            if i == (len(nums)-1):
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i]*suffix[i+1]

        l = []
        for i in range(len(nums)):
            if i == 0:
                l.append(suffix[i+1])
            elif i == (len(nums)-1):
                l.append(prefix[i-1])
            else:
                l.append(prefix[i-1]*suffix[i+1])
        
        return l


