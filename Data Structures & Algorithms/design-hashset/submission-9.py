class MyHashSet:

    def __init__(self):
        self.l = [None]*10
        self.size = 10
        self.filled = 0       

    def add(self, key: int) -> None:
     a = self.find_the_element(key)
     if a == (-1):
        if self.filled < self.size:
            index = self.hash_function(key)
            if self.l[index] in [None,'removed']:
                self.l[index] = key
                self.filled += 1
            else:
                while self.l[index] not in [None,'removed']:
                    index = index + 1
                    index = index % self.size 
                self.l[index] = key
                self.filled += 1
        
        elif self.filled == self.size:
            l2 = [None] * self.size * 2
            self.size = self.size * 2

            for j in self.l:
               if j not in [None,'removed']: 
                    i = self.hash_function(j)
                    if l2[i] == None:
                        l2[i] = j
                    else:
                        while l2[i] != None:
                            i = i + 1
                            i = i % self.size 
                        l2[i] = j
            
            index = self.hash_function(key)
            if l2[index] == None:
                l2[index] = key
                self.filled += 1
            else:
                while l2[index] != None:
                    index = index + 1
                    index = index % self.size 
                l2[index] = key
                self.filled += 1
            
            self.l = l2
            

    def remove(self, key: int) -> None:
        a = self.find_the_element(key)
        if a!= (-1):
            self.l[a] = 'removed'
            self.filled = self.filled - 1

        

    def contains(self, key: int) -> bool:
        a = self.find_the_element(key)
        print(a)
        if a != (-1):
            return True
        else:
            return False


    def hash_function(self, key):
        index = hash(key) % (self.size)
        return index


    def find_the_element(self, key):
        poss_index = self.hash_function(key)

        if self.l[poss_index] == key:
            return poss_index
        
        elif self.l[poss_index] == None:
            return -1
        
        else:
            k = poss_index
            while True:
                poss_index += 1
                poss_index = poss_index % self.size

                if self.l[poss_index] == key:
                    return poss_index
                
                elif self.l[poss_index] == None:
                    return -1

                elif poss_index == k:
                    return -1
            
