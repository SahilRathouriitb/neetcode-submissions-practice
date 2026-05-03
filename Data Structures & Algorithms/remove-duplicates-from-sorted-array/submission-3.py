class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        store = []
        k = 0

        for i in range(len(nums)):

            if (i >0) and (nums[i] == nums[i-1]):
                store.append(i)
            else:
                k += 1

        print(store)
        # Now we have the indexes which hold duplicate items
        i = 0
        while i < len(store): 

            if i == (len(store) -1):
                for  j in range(store[i], len(nums)):
                    nums[j-(i+1)] = nums[j]
            else:
                for  j in range(store[i], store[i+1]):
                    nums[j-(i+1)] = nums[j]
            i += 1
            
        print(k)
        print(nums)
        return k



