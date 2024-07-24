class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        newNode = Node(value)
        self.length = 1
        self.head = newNode
        self.tail = newNode

    def Append(self, value):
        temp = Node(value)
        if self.length == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1

    def Pop(self):
        temp = self.head
        if self.length == 0:
            return None
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def Prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def PopFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def Get(self, index):
        if self.length <= index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def Set(self, value, index):
        temp = self.Get(index)
        if temp:
            temp.value = value
            return True
        return False

    def Insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.Prepend(value)
        if index == self.length:
            self.Append(value)
        newNode = Node(value)
        temp = self.Get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

    def Remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.PopFirst()
        if index == self.length - 1:
            self.Pop()
        prev = self.Get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def Reverse(self):
        prev = None
        temp = self.head
        while (temp):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        self.head, self.tail = self.tail, self.head

    def __str__(self):
        res=""
        temp = self.head
        while temp != None:
            res += str(temp.value)+"\n"
            temp = temp.next
        return res


linkedlist = LinkedList(4)
linkedlist.Append(5)
linkedlist.Append(6)
linkedlist.Append(7)
linkedlist.Append(8)
linkedlist.Append(9)
linkedlist.Append(10)

print(linkedlist.Pop().value)
print("Linked List: ")
linkedlist.Reverse()
print(linkedlist)
