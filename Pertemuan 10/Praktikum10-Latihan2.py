# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST 
class Node: 
    # Method konstruktor untuk menginisialisasi isi node.
    def __init__(self, data): 
        # Menyimpan nilai data pada node. 
        self.data = data      # nilai pada node 
        # Menginisialisasi child kiri sebagai kosong. 
        self.left = None      # child kiri 
        # Menginisialisasi child kanan sebagai kosong. 
        self.right = None     # child kanan 
 

# Fungsi insert untuk BST 
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    # Mengembalikan root setelah proses penyisipan selesai. 
    return root 
 

# Fungsi preorder untuk melihat bentuk tree 
def preorder(root): 
    # Cek apakah node saat ini ada sebelum diproses. 
    if root is not None: 
        # Menampilkan data root terlebih dahulu. 
        print(root.data, end=" ") 
        # Menelusuri subtree kiri setelah root. 
        preorder(root.left) 
        # Menelusuri subtree kanan setelah subtree kiri. 
        preorder(root.right) 
 

# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    # Cek apakah node saat ini ada sebelum ditampilkan. 
    if root is not None: 
        # Menampilkan posisi node sesuai level kedalaman tree. 
        print("   " * level + f"{posisi}: {root.data}") 
        # Menampilkan subtree kiri dengan level bertambah satu. 
        tampil_struktur(root.left, level + 1, "L") 
        # Menampilkan subtree kanan dengan level bertambah satu. 
        tampil_struktur(root.right, level + 1, "R") 

# ----------------------------- 
# Program utama 
# ----------------------------- 
# Menginisialisasi root BST dengan nilai kosong. 
root = None 

# Data dimasukkan berurutan naik 
# Menyediakan data yang akan membuat BST menjadi tidak seimbang. 
data_list = [10, 20, 30] 

# Melakukan perulangan untuk memasukkan setiap data ke BST. 
for data in data_list: 
    # Menyisipkan data ke BST dan memperbarui root. 
    root = insert(root, data) 

# Menampilkan judul traversal preorder BST. 
print("Preorder BST:") 
# Menjalankan traversal preorder. 
preorder(root) 

# Menampilkan judul struktur BST. 
print("\n\nStruktur BST:") 
# Menampilkan struktur BST secara visual sederhana. 
tampil_struktur(root) 
