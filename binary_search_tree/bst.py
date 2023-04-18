class BinarySearchTree:

    def __init__(self) -> None:
        self._size = 0
        self._root = None

    class _BSTNode:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def add(self, key, value) -> None:
        new_node = self._BSTNode(key, value)
        if (self._root==None):
            self._root = new_node
            return
        prev = None
        temp = self._root
        while (temp != None):
            if (temp.key > key):
                prev = temp
                temp = temp.left
            elif(temp.key < key):
                prev = temp
                temp = temp.right

        if (prev.key > key):
            prev.left = new_node
        else:
            prev.right = new_node

    def inorder_walk(self):
        temp = self._root
        stack = []
        result = []
        while (temp != None or not (len(stack) == 0)):
            if (temp != None):
                stack.append(temp)
                temp = temp.left
            else: 
                temp = stack.pop()
                print(str(temp.value) + " ", end="")
                result.append(temp.key)
                temp = temp.right
            
        return result

    def calc_size(self, node):
        if node is None:
            return 0
        else:
            return (self.calc_size(node.left) + self.calc_size(node.right) + 1)

    def size(self):
        self._size = self.calc_size(self._root)
        return self._size
    
    def search(self, key):
        if self._root is None or self._root.key == key:
            return self._root.value
        
        if self._root.key < key:
            return self.search(self._root.right, key)
        
        return self.search(self._root.left, key)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add(10, "Value for 10")
    bst.add(52, "Value for 52")
    bst.add(5, "Value for 5")
    bst.add(8, "Value for 8")
    bst.add(1, "Value for 1")
    bst.add(40, "Value for 40")
    bst.add(30, "Value for 30")
    bst.add(45, "Value for 45")  

    print(bst.inorder_walk()) 

    print(bst.size())

    print(bst.search(30))