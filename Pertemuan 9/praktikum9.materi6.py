#===================================
# Latihan 6: Struktur Organisasi Perusahaan
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

root = Node("Direktur") # Membuat root

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Karyawan A1")
root.left.right = Node("Karyawan A2")
root.right.left = Node("Karyawan B1")

print("Struktur Organisasi Perusahaan:")
preorder(root)