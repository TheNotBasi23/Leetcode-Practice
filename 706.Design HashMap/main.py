class MyHashMap:

    def __init__(self):
        self.balanceFactor = 0.5
        self.hashmapSize = 10
        self.hashmap = [[] for i in range(self.hashmapSize)]
        self.numElements = 0

    def put(self, key: int, value: int) -> None:

        for i,(k,v) in enumerate(self.hashmap[key % self.hashmapSize]):
            if k == key:
                self.hashmap[key % self.hashmapSize][i] = (key,value)
                return



        if float(self.numElements) >= self.balanceFactor * self.hashmapSize:
            allElements = [(k,v) for arr in self.hashmap for k,v in arr]
            allElements.append((key,value))
            self.hashmapSize *= 2
            self.hashmap = [[] for i in range(self.hashmapSize)]
            self.numElements = 0
            for k,v in allElements:
                self.put(k,v)

        else:
            self.hashmap[key %self.hashmapSize].append((key,value))
            self.numElements += 1

    def get(self, key: int) -> int:
        for hKey,value in self.hashmap[key%self.hashmapSize]:
            if key == hKey:
                return value
        else:
            return -1
    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap[key % self.hashmapSize])):
            if self.hashmap[key % self.hashmapSize][i][0] == key:
                self.hashmap[key % self.hashmapSize].pop(i)
                self.numElements -= 1
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)