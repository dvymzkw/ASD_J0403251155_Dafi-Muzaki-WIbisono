# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang 
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
 

# Fungsi rotasi kanan 
def rotate_right(x): 
    # x adalah root lama 
    y = x.left         # y adalah child kiri x 
    T2 = y.right       # subtree kanan milik y disimpan sementara 
 
    # Proses rotasi 
    y.right = x        # x menjadi child kanan dari y 
    x.left = T2      # child kiri x diganti dengan T2 
 
    # y menjadi root baru 
    return y 

# ----------------------------- 
# Program utama 
# ----------------------------- 

# Membuat tree yang tidak seimbang: 
# 10 -> 20 -> 30 
# Membuat root awal dengan nilai 30. 
root = Node(30) 
# Menambahkan node 20 sebagai child kiri root. 
root.left = Node(20) 
# Menambahkan node 10 sebagai child kiri dari node 20. 
root.left.left = Node(10) 

# Menampilkan preorder sebelum rotasi kanan dilakukan. 
print("Preorder sebelum rotasi kiri:") 
# Menampilkan isi tree sebelum rotasi. 
preorder(root) 

# Menampilkan struktur tree sebelum rotasi kanan. 
print("\n\nStruktur sebelum rotasi kiri:") 
# Menampilkan bentuk tree sebelum rotasi. 
tampil_struktur(root) 

# Melakukan rotasi kiri pada root 
# Memperbarui root dengan hasil rotasi kanan. 
root = rotate_right(root) 

# Menampilkan preorder setelah rotasi kanan dilakukan. 
print("\nPreorder sesudah rotasi kanan:") 
# Menampilkan isi tree setelah rotasi. 
preorder(root) 

# Menampilkan struktur tree setelah rotasi kanan. 
print("\n\nStruktur sesudah rotasi kanan:") 
# Menampilkan bentuk tree setelah rotasi. 
tampil_struktur(root) 
