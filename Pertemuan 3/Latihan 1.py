#Latihan 1
#Dafi Muzaki Wibisono (J0403251155)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, key):
        temp = self.head

        if temp	and	temp.data == key:
            self.head = temp.next
            temp = None
            return
    
        prev = None

        while temp and temp.data !=	key:
            prev = temp 
            temp = temp.next
    
        if temp	is None:
            return
    
        prev.next =	temp.next
        temp = None

# Contoh Penggunaan
ll = LinkedList()
data_input = input("(Latihan 1) Masukkan elemen ke dalam Linked List: ")
data = data_input.strip().split()
for i in data:
    ll.insert_at_end(int(i))
ll.delete_node(int(input("Masukkan elemen yang akan dihapus: ")))
ll.display() 