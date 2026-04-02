class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 0
            dict[i] = dict[i]+1

        a = list(dict.values())
        a.sort()
        b = a[-k:]
        c = []
        for i in dict:
            if dict[i] in b:
                c.append(i)

        return c         
        
            
        

         