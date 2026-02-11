#Latihan 3
#Dafi Muzaki Wibisono (J0403251155)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Menyimpan node terakhir untuk traversing mundur

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

    def search(self, key):
        temp = self.head 
        while temp:
            if temp.data == key:
                print(f"Element {key} found.")
                return True 
            temp = temp.next
        print(f"Element {key} not found.") 
        return False 

# Contoh Penggunaan
dll = DoubleLinkedList()
data_input = input("(Latihan 3) Masukkan elemen ke dalam Double Linked List: ")
data = data_input.strip().split()
for i in data:
    dll.insert_at_end(int(i))
dll.search(int(input('Masukkan elemen yang dicari: ')))
dll.display_forward()
dll.display_backward()