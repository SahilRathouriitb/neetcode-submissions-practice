class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hash = {1:'ok'}
        nums = set(nums)
    
        for i in nums:

            if i > 0:
            
                if i not in hash:
                    hash[i+1] = 'ok'
                
                else:
                    hash.pop(i)
                    hash[i+1] = 'ok'
        print(hash)
        return min(hash.keys())