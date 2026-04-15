#===================================
# Latihan 1: Traversal Inorder
#===================================

# Class Node digunakan sebagai dasar untuk tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai  node
        self.left = None # Child kiri
        self.right = None # Child kanan

# Traversal Inorder
def inorder(node):
    if node is not None:
        inorder(node.left) # Melihat subtree kiri
        print(node.data, end=" ") # Melihat root
        inorder(node.right) # Melihat subtree kanan

root = Node("A") # Membuat root

# Child level 1
root.left = Node("B")
root.right = Node("C")

# Child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

inorder(root)