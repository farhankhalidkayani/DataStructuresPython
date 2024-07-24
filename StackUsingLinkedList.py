class Item:
    def __init__(self, value):
        self.val = value
        self.next = None


class Stack:
    def __init__(self, value):
        newItem = Item(value)
        self.length = 1
        self.top = newItem

    def printList(self):
        temp=self.top
        while temp:
            print(temp.val)
            temp=temp.next

    def push(self, value):
        newItem = Item(value)
        if self.top is None:
            self.top = newItem
        else:
            newItem.next = self.top
            self.top = newItem
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp

    def peek(self):
        return self.top.val

def main():
    stack=Stack(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.printList()
    print()
    print(stack.pop().val)
    print()
    stack.printList()
    print()
    print(stack.peek())
    print()
    stack.printList()
    print()
    stack.push(10)
    stack.printList()

main()

