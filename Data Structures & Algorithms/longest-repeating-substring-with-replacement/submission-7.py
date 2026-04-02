class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0 
        right = 0 
        dic = {}
        answer = 1 
        temp = -1

        while right < len(s):

            if temp != right:
                if s[right] in dic:
                    dic[s[right]] = dic[s[right]] + 1

                else:
                    dic[s[right]] = 1

            
            window_size = right - left + 1
            print(left, right, dic)

            most_frequent = 0
            for i in dic:
                most_frequent = max(most_frequent, dic[i])
            
            temp = right 
            
            if window_size - most_frequent <= k:
                answer = max(answer, window_size)
                right = right + 1

            else:
                # This is the condition for invalid
                # We will move the left pointer in 
                dic[s[left]] = dic[s[left]] - 1
                left = left + 1
            
            

        
        return answer
                
            

