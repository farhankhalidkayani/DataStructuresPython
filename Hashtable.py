class HashTable:
    def __init__(self,size=7) -> None:
        self.myMap=[None]*size

    def __hash(self,key):
        myHash=0
        for letter in key:
            myHash=(myHash+ord(letter)*23)%len(self.myMap)
        return myHash
    def set(self,key,value):
        index=self.__hash(key)
        if self.myMap[index]==None:
            self.myMap[index]=[]
        self.myMap[index].append([key,value])

    def get(self,key):
        index=self.__hash(key)
        if self.myMap[index] is not None:
            for i in range(len(self.myMap[index])):
                if self.myMap[index][i][0]==key:
                    return self.myMap[index][i][1]
        return None
    def keys(self):
        AllKeys=[]
        for i in range(len(self.myMap)):
            if self.myMap[i] is not None:
                for j in range(len(self.myMap[i])):
                    AllKeys.append(self.myMap[i][j][0])
        return AllKeys

myHashtable=HashTable()
myHashtable.set("Farhan",1)
myHashtable.set("Hannan",2)
print(myHashtable.get("Farhan"))
print(myHashtable.get("Hannan"))
print(myHashtable.keys())