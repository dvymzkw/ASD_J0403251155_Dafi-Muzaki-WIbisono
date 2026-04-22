# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
# ========================================================== 
 
# Class Node 
class Node: 
    # Method konstruktor untuk menginisialisasi node tree. 
    def __init__(self, data): 
        # Menyimpan nilai data pada node. 
        self.data = data 
        # Menginisialisasi child kiri dengan nilai kosong. 
        self.left = None 
        # Menginisialisasi child kanan dengan nilai kosong. 
        self.right = None 
 

# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    # Cek apakah node ada sebelum diproses. 
    if root is not None: 
        # Menampilkan data root terlebih dahulu. 
        print(root.data, end=" ") 
        # Menelusuri subtree kiri. 
        preorder(root.left) 
        # Menelusuri subtree kanan. 
        preorder(root.right) 
 

# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    # Cek apakah node ada sebelum ditampilkan. 
    if root is not None: 
        # Menampilkan posisi dan data node sesuai level kedalaman. 
        print("   " * level + f"{posisi}: {root.data}") 
        # Menampilkan subtree kiri dengan level berikutnya. 
        tampil_struktur(root.left, level + 1, "L") 
        # Menampilkan subtree kanan dengan level berikutnya. 
        tampil_struktur(root.right, level + 1, "R") 
 

# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara 
 
    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2 
 
    # y menjadi root baru 
    return y 

# ----------------------------- 
# Program utama 
# ----------------------------- 

# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
# Membuat root awal dengan nilai 10. 
root = Node(10) 
# Menambahkan node 20 sebagai child kanan root. 
root.right = Node(20) 
# Menambahkan node 30 sebagai child kanan dari node 20. 
root.right.right = Node(30) 

# Menampilkan preorder sebelum rotasi kiri dilakukan. 
print("Preorder sebelum rotasi kiri:") 
# Menampilkan isi tree sebelum rotasi. 
preorder(root) 

# Menampilkan struktur tree sebelum rotasi kiri. 
print("\n\nStruktur sebelum rotasi kiri:") 
# Menampilkan bentuk tree sebelum rotasi. 
tampil_struktur(root) 

# Melakukan rotasi kiri pada root 
# Memperbarui root dengan hasil rotasi kiri. 
root = rotate_left(root) 

# Menampilkan preorder setelah rotasi kiri dilakukan. 
print("\nPreorder sesudah rotasi kiri:") 
# Menampilkan isi tree setelah rotasi. 
preorder(root) 

# Menampilkan struktur tree setelah rotasi kiri. 
print("\n\nStruktur sesudah rotasi kiri:") 
# Menampilkan bentuk tree setelah rotasi. 
tampil_struktur(root) 
