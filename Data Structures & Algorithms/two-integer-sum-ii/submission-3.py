class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            k = target - numbers[i]
            for j in range(len(numbers)):
                if i != j:

                    if numbers[j] == k:
                        return [i+1,j+1]            