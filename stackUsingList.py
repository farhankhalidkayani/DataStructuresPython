
class Stack:
    def __init__(self, value):
        self.stack=[]
        self.stack.append(value)
    def printList(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        temp=self.stack.pop()
        return temp

    def peek(self):
        return self.stack[-1]

def main():
    stack=Stack(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.printList()
    print()
    print(stack.pop())
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