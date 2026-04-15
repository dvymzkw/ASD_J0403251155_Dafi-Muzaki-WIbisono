#===================================
# Latihan 3: Traversal Preorder
#===================================

# Class Node digunakan sebagai dasar untuk tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan

# Traversal Preorder
def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Melihat root
        preorder(node.left) # Melihat subtree kiri
        preorder(node.right) # Melihat subtree kanan

root = Node("A") # Membuat root

# Child level 1
root.left = Node("B")
root.right = Node("C")

# Child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

preorder(root)