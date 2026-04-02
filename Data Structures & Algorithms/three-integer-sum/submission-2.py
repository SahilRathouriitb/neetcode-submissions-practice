class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        l = []
        for s in range(len(nums)):

            if (s != 0) and (nums[s] == nums[s-1]):
                continue
            target = 0 - nums[s]
            i = s + 1
            j = len(nums) - 1

            while i < j:
                
                
                    
                if nums[i] + nums[j] == target:
                    l.append([nums[s], nums[i], nums[j]])
                    i = i+1
                    while (nums[i] == nums[i-1]) and i<j:
                        i = i+1
                    
                        
                elif nums[i]+ nums[j] < target:
                    i = i+1
                        
                else:
                    j = j - 1


        
        return l