#===================================
# Latihan 1: Membuat Node
#===================================

# Class Node digunakan sebagai dasar untuk tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan

# Traversal Postorder
def postorder(node):
    if node is not None:
        postorder(node.left) # Melihat subtree kiri
        postorder(node.right) # Melihat subtree kanan
        print(node.data, end=" ") # Melihat root

root = Node("A") # Membuat root

# Child level 1
root.left = Node("B")
root.right = Node("C")

# Child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

postorder(root)