class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        store = []
        temp = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    
        n = len(nums)
        self.permu(dic, store, temp, n)
        return store

    def permu(self, dic, store,temp, n):
        if len(temp) == n:
            store.append(temp.copy())
            return

        for i in dic:
            if dic[i] == 0:
                continue

            temp.append(i)
            dic[i] -= 1
            self.permu(dic, store, temp, n)
            dic[i] += 1
            temp.pop()
            

        

        
 
        