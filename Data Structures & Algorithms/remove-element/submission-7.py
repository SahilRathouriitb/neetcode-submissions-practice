class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        c = []
        for i in nums:
             c.append(i)
        
        for i in c:
            if i == val:
                nums.remove(i)
        return len(nums)