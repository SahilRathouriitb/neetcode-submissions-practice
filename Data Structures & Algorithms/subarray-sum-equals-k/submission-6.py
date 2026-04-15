class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
      dic = {0:1}
      count = 0
      sum = 0

      for i in nums:
        sum = sum + i
        if (sum-k) in dic:
            count = count + dic[sum-k]

        if sum in dic:
            dic[sum] = dic[sum] + 1
        else:
            dic[sum] = 1

      return count     
