#==========================
#Implementasi Dasar: Node pada Linked List
#Dafi Muzaki Wibisono
#J0403251155
#TPL B2
#==========================

#Membuat class Node (merupakan unit dasar dari Linked List)
class Node:
    def __init__(self, data): #Constructor
        self.data = data #Menyimpan nilai
        self.next = None #Pointer ke note berikutnya (awal = none)

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node('B')
nodeC = Node("C")

# 2) Menghubungkan Node: A > B > C > None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal: Menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)     #Menampilkan data pada node saat ini
    current = current.next  #Pindah ke node berikutnya

#============================
#Implementasi Dasar: Linked List + Insert Awal
#============================

class LinkedList:
    def __init__(self):
        self.head = None #Awalnya kosong

    def insert_awal(self, data): #Push dalam satck
        # 1) Buat node baru
        nodeBaru = Node(data) #Panggil class node

        # 2) Node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) Head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #Pop dalam stack
        data_terhapus = self.head.data #Peek dalam stack
        #Menggeser head ke node berikutnya
        self.head = self.head.next
        print('Node yang dihapus adalah: ', data_terhapus)
    
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("===List Baru===")
ll = LinkedList() #Instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()