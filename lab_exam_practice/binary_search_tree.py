class Node:
  def __init__(self, data):
    self.data = data
    self.next_left = None
    self.next_right = None


class BinarySearchTree:
  def __init__(self, nodes=None):
    self.head = None
  
  def size(self):
    nodes =  self.inorder_walk()
    return len(nodes)

  def add(self, key, value=None):
    node = Node(key)
    if self.head is None:
      self.head = node
      # print("Created first Node: ")
      return

    prev_node = None
    pointer_node = self.head
    while pointer_node != None:

      if key >= pointer_node.data:
          prev_node = pointer_node
          pointer_node = pointer_node.next_right
      elif key <= pointer_node.data:
          prev_node = pointer_node
          pointer_node = pointer_node.next_left
    if key < prev_node.data:
      prev_node.next_left = node
    else:
      prev_node.next_right = node
    # print("Created Secondary Node", prev_node)


  # Traversal
  def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.next_left)
            res.append(root.data)
            # print(root.data)
            res = res + self.inorderTraversal(root.next_right)
        return res

  def inorder_walk(self):
    root = self.head
    return self.inorderTraversal(root)

  def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            # print(root.data)
            res = res + self.preorderTraversal(root.next_left)
            res = res + self.preorderTraversal(root.next_right)
        return res

  def preorder_walk(self):
    root = self.head
    return self.preorderTraversal(root)


  def postorderTraversal(self, root):
        res = []
        if root:
            # print(root.data)
            res = res + self.postorderTraversal(root.next_left)
            res = res + self.postorderTraversal(root.next_right)
            res.append(root.data)
        return res

  def postorder_walk(self):
    root = self.head
    return self.postorderTraversal(root)

  def smallest(self):
    nodes = self.inorder_walk()
    return (nodes[0], f"Value for {nodes[0]}")

  def largest(self):
    nodes = self.inorder_walk()
    return (nodes[-1], f"Value for {nodes[-1]}")

  def search(self, key):
    nodes = self.inorder_walk()
    if key in nodes:
      return f"Value for {key}"
    else:
      # return f"No value for {key}"
      return False

  def minimumValueNode(self, node):
    current = node

    while(current.next_left is not None):
      current = current.next_left

    return current

  def maximumValueNode(self, node):
    current = node
    while(current.next_right is not None):
      current = current.next_right

    return current

  def remove(self, key):
    node = self.head
    return self.remove_key(node, key)    
    

  def remove_key(self, root, key):
    if root is None:
      return "Tree is empty"
    
    if key < root.data:
      root.next_left = self.remove_key(root.next_left, key)
    
    elif key > root.data:
      root.next_right = self.remove_key(root.next_right, key)
    
    else:    
      if root.next_left is None:
        temp = root.next_right
        root = None
        return temp
      elif root.next_right is None:
        temp = root.next_left
        root = None
        return temp

      # temp = self.minimumValueNode(root.next_right)
      temp = self.maximumValueNode(root.next_left)

      root.data = temp.data

      root.next_left = self.remove_key(root.next_left, temp.data)
    return root



  def __repr_(self):
    nodes = self.inorder_walk()
    return " -> ".join(nodes)


# bst.setUp()
bst = BinarySearchTree()

bst.add(10)
bst.add(key=52)
bst.add(key=5)
bst.add(key=8)
bst.add(key=1)
bst.add(key=40)
bst.add(key=30)
bst.add(key=45)

size = bst.size()
print(size)
print("Inorder  : ", bst.inorder_walk())
print("Preorder  : ", bst.preorder_walk())
print("Postorder  : ", bst.postorder_walk())
print("Smallest : ", bst.smallest())
print("Largest : ", bst.largest())

print(bst.search(40))
bst.remove(key=40)

print("Inorder  : ", bst.inorder_walk())
print("PostOrder", bst.preorder_walk())