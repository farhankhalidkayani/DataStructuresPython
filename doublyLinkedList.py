class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.length = 1
        self.head = newNode
        self.tail = newNode

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def empty(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def setValue(self,index,value):
        temp=self.get(index)
        if temp:
            temp.val=value
            return True
        return False

    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        newNode = Node(value)
        prev=self.get(index-1)
        after=prev.next
        prev.next=newNode
        after.prev=newNode
        newNode.next=after
        newNode.prev=prev
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.popFirst()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        prev=temp.prev
        after=temp.next
        prev.next=after
        after.prev=prev
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp



def __main__():
    double = DoublyLinkedList(5)
    double.append(6)
    double.append(7)
    double.append(8)
    double.append(9)
    double.prepend(1)
    double.printList()
    print()
    double.pop()
    double.popFirst()
    double.printList()
    print()
    print(double.get(2).val)
    print()
    double.insert(2,9)
    double.printList()
    print()
    print(double.remove(2).val)
    print()
    double.printList()



__main__()
