class Pair:
    def __init__(self, key, val): # key and val is assumed to be strings in this implementation
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.size = 0 # numbers of keys in hash map
        self.capacity = 2 # the capacity of the hash map. Optimally it should be a prime number
        self.map = [None, None] # To designate it is empty. This is the map itself

    def hash(self, key): # given some key convert it to some integer that fits in our capacity of 2
        index = 0
        for c in key:
            index += ord(c) # converts the character to the ASCII character
        return index % self.capacity
    

#searching for a key
def get(self, key):
    index = self.hash(key)

    while self.map[index] != None:
        if self.map[index].key == key:
            return self.map[index].val
        index += 1
        index = index % self.capacity
    return None

#inserting a key
def put(self, key, val):
    index = self.hash(key)

    while True:
        if self.map[index] == None:
            self.map[index] = Pair(key, val)
            self.size += 1
            if self.size >= self.capacity // 2:
                self.rehash()
            return
        elif self.map[index].key == key:
            self.map[index].val = val
            return
        index += 1
        index = index % self.capacity

#Removing a key
def remove(self, key):
    if not self.get(key):
        return
    
    index = self.hash(key)
    while True:
        if self.map[index].key == key:
            # Removing an element using open-addressing actually causes a bug,
            # because we may create a hole in the list, and our get() may 
            # stop searching early when it reaches this hole.
            self.map[index] = None
            self.size -= 1
            return
        index += 1
        index = index % self.capacity

#Rehashing

def rehash(self):
    self.capacity = 2 * self.capacity
    newMap = []
    for _ in range(self.capacity):
        newMap.append(None)

    oldMap = self.map
    self.map = newMap
    self.size = 0
    for pair in oldMap:
        if pair:
            self.put(pair.key, pair.val)

#Printing all pairs

def print(self):
    for pair in self.map:
        if pair:
            print(pair.key, pair.val)