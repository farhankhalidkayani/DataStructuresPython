class Node:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        newNode=Node(value)
        if self.root is None:
            self.root=newNode
            return True
        temp=self.root
        while True:
            if temp.val==newNode.val:
                return False
            if newNode.val>temp.val:
                if temp.right is None:
                    temp.right=newNode
                temp=temp.right
            else :
                if temp.left is None:
                    temp.left=newNode
                    return True
                temp=temp.left
    def contains(self,value):
        temp=self.root
        while temp is not None:
            if temp.val>value:
                temp=temp.left
            elif temp.val<value:
                temp=temp.right
            elif temp.val==value:
                return True
        return False
            

bst=BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)
print(bst.contains(27))
