#===================================
# Latihan 1: Membuat Node
#===================================

# Class Node digunakan sebagai dasar untuk tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai node
        self.left = None # Child kiri
        self.right = None # Child kanan

root = Node("A") # Membuat root

print(root.data)