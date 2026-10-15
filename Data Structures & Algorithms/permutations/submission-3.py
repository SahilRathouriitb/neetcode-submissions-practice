class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        store = []
        self.permu(nums, 0, store)
        return store

    def permu(self,arr,i, store):
        if i == len(arr):
            store.append(arr[:])
            return 

        for k in range(i, len(arr)):
            arr[i],arr[k] = arr[k], arr[i]
            self.permu(arr, i+1, store)

            #backtrack, revert the swap
            arr[i], arr[k] = arr[k], arr[i]
        
 
        