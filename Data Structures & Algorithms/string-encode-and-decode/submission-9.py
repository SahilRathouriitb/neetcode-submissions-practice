class Solution:

    def encode(self, strs: List[str])->str:
        
        if len(strs) == 0:
            return "iceeecream"
        else:
            encode = ""

            if len(strs)==0:
                return None
            for i in strs:
                encode = encode + i + '@!'

            return encode[:-2]

    def decode(self, s: str) -> List[str]:

            if s== "iceeecream":
                a = [1]
                a.pop()
                return a
            else:
                return s.split('@!')