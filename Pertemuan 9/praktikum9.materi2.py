#===================================
# Latihan 2: Membuat child
#===================================

# Class Node digunakan sebagai dasar untuk tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan

root = Node("A") # Membuat root

# Child level 1
root.left = Node("B")
root.right = Node("C")

# Child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Node:", root.data)
print("Node kiri root:", root.left.data)
print("Node kanan root:", root.right.data)
print("Node kiri dari B:", root.left.left.data)
print("Node kanan dari B:", root.left.right.data)
print("Node kiri dari C:", root.right.left.data)
print("Node kanan dari C:", root.right.right.data)