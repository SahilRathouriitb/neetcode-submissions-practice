class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
                a = 1
                for j in range(len(nums)):

                    if i != j:
                        a = a * nums[j]

                l.append(a)

        return l
