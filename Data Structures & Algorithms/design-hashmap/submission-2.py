class MyHashMap:

    def __init__(self):
        self.filled = 0
        self.size = 10
        self.l = self.make_dic()


    def make_dic(self):   
        k = []
        for i in range(self.size):
            k.append(Node()) 
        return k
        

    def resize(self, size):
        k = []
        for i in range(size):
            k.append(Node())

        # Rehashing missing in this as per new size
        for i in range(len(self.l)):
            index = self.hash_function(self.l[i].key, size)
            if k[index].key == None:
                k[index].key = self.l[i].key
                k[index].value = self.l[i].value

            else:
                while True:
                    index = index + 1
                    index = index % size

                    if k[index].key == None:
                        k[index].key = self.l[i].key
                        k[index].value = self.l[i].value
                        break

        self.l = k
        self.size = size 

        
    def hash_function(self, key, size):
        index = hash(key)% size
        return index
    

    def find_the_element(self, key):
        poss_index = self.hash_function(key, self.size)
        s = poss_index
        if self.l[poss_index].key == key:
            return poss_index, self.l[poss_index].value

        else:
            while self.l[poss_index].key not in [None,'removed']:
                poss_index += 1
                poss_index = poss_index % self.size
                if self.l[poss_index].key == key:
                    return poss_index,self.l[poss_index].value
                if poss_index == s:
                    return -1,-1

            return -1,-1

    

    def put(self, key: int, value: int) -> None:
        
        if self.filled == self.size:
            self.resize(self.size*2)

        index = self.hash_function(key,self.size)

        if self.l[index].key == key:
            self.l[index].value = value

        elif self.l[index].key in [None,'removed']:
            self.l[index].key = key
            self.l[index].value = value
            self.filled += 1

        else:
            while True:
                index = index + 1
                index = index % self.size

                if self.l[index].key in [None,'removed']:
                    self.l[index].key = key
                    self.l[index].value = value
                    self.filled += 1
                    break
                    

    

    def get(self, key: int) -> int: 
        a,b = self.find_the_element(key)
        return b 


    def remove(self, key: int) -> None:
        a,b = self.find_the_element(key)
        if a != -1:
            self.l[a].key = 'removed'
            self.filled -= 1
        

class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value

