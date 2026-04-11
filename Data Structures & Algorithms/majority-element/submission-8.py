class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic = {}

        for i in nums:

            if len(dic) == 0:
                dic[i] = 1

            elif len(dic) == 1:
                if i in dic:
                    dic[i] = dic[i] + 1

                else:
                    dic_copy = dic
                    for j in dic_copy:
                        dic[j] = dic[j] - 1
                        
                        if dic[j] == 0:
                            dic = {}

        l = [i for i in dic]
        return l[0]                       
                    
               

               

                        