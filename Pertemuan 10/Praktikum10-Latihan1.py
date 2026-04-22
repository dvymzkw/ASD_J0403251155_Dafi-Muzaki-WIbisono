#================================
# Dafi Muzaki Wibisono
# J0403251155
# Latihan 1-3: BST
#================================

# Mendefinisikan class Node untuk merepresentasikan setiap simpul pada BST.
class Node:
    # Method konstruktor untuk menginisialisasi data dan anak kiri/kanan.
    def __init__(self, data):
        # Menyimpan nilai data ke dalam node.
        self.data = data
        # Menginisialisasi child kiri dengan nilai kosong.
        self.left = None
        # Menginisialisasi child kanan dengan nilai kosong.
        self.right = None

# Mendefinisikan fungsi untuk menambahkan data ke dalam BST.
def insert(root, data):
    # Jika root belum ada, buat node baru sebagai root.
    if root is None:
        return Node(data)

    # Jika data lebih kecil dari root, masukkan ke subtree kiri.
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar dari root, masukkan ke subtree kanan.
    elif data > root.data:
        root.right = insert(root.right, data)

    # Mengembalikan root setelah proses insert selesai.
    return root

# Mengisi data BST
# Menginisialisasi root awal dengan nilai kosong.
root = None
# Menyediakan daftar data yang akan dimasukkan ke BST.
data_list = [50, 30, 70, 20, 40, 60, 80]

# Melakukan perulangan untuk memasukkan setiap data ke BST.
for data in data_list:
    # Memperbarui root dengan hasil penyisipan data.
    root = insert(root, data)

# Menampilkan pesan bahwa BST sudah berhasil dibuat.
print("BST berhasil dibuat.")

# Mendefinisikan fungsi inorder untuk menampilkan isi BST secara terurut.
def inorder(root):
    # Memastikan node saat ini tidak kosong sebelum ditelusuri.
    if root is not None:
        # Menelusuri subtree kiri terlebih dahulu.
        inorder(root.left)
        # Menampilkan data node saat ini.
        print(root.data, end=" ")
        # Menelusuri subtree kanan setelah itu.
        inorder(root.right)

# Menampilkan judul hasil traversal inorder.
print("Hasil Inorder: ")
# Memanggil fungsi inorder untuk mencetak isi BST.
inorder(root)

# Mendefinisikan fungsi pencarian nilai pada BST.
def search(root, key):
    # Jika node tidak ditemukan, kembalikan False.
    if root is None:
        return False
    
    # Jika data pada root sama dengan key, berarti data ditemukan.
    if root.data == key:
        return True
    # Jika key lebih kecil, cari pada subtree kiri.
    elif key < root.data:
        return search(root.left, key)
    # Jika key lebih besar, cari pada subtree kanan.
    else:
        return search(root.right, key)
# Uji Pencarian
# Menentukan nilai yang ingin dicari pada BST.
key = 100
# Jika fungsi search bernilai True, tampilkan pesan ditemukan.
if search(root, key):
    print("Data ditemukan.")
# Jika tidak ditemukan, tampilkan pesan sebaliknya.
else:
    print("Data tidak ditemukan.")
