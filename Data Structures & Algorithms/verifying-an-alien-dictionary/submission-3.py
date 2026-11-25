class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        map = {}
        j = 0
        for i in order:
            map[i] = j
            j += 1
        print(map)
        # We need to find the length of the longest word
        count = 0 
        for s in words:
            count = max(count, len(s))

        
        

        for j in range(len(words)-1):

            for i in range(len(words[j])):

                if i >= len(words[j+1]):
                    return False

                if map[words[j][i]] == map[words[j+1][i]]:
                    continue

                if map[words[j][i]] > map[words[j+1][i]]:
                    return False

                if map[words[j][i]] < map[words[j+1][i]]:
                    break

                

        
        return True