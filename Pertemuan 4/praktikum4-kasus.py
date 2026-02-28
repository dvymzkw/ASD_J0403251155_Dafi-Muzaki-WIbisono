#==================================
# Dafi Muzaki WIbisono
# J0403251155
# TPL B2
#==================================

# Studi Kasus: Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue: Memindahkan pointer rear 
# Dequeue: Memindahkan pointer front
# Front-> A -> B -> C -> Rear

#===================================

# Mendefinisikan Node (Unit dasar Linked List)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim # Menyimpan NIM Mahasiswa
        self.nama = nama # Menyimpan Nama Mahasiswa
        self.next = None # Pointer ke node berikutnya

# Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None
    
    # Menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        # Jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika queue tidak kosong, maka data baru diletakkan stelah rear kemudian dijadikan sebagai rear 
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print('Antrian kosong. Tidak ada mahasiswa yang dilayani.')
            return None

        # Lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        # Menggeser pointer front ke next front
        self.front = self.front.next

        # Jika front menjadi none (data terakhir mahasiswa yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):
        print('Daftar antrian mahasiswa (front -> rear)')
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

    # Program Utama

def main():

    #Instantiasi queue
    q = queueAkademik()

    while True:
        print('=== Sistem Antrian Akademik ===')
        print('1. Tambah Mahasiswa')
        print('2. Layani Mahasiswa')
        print('3. Lihat Antrian')
        print('4. Keluar')

        pilihan = input('Pilih menu (1-4): ').strip()

        if pilihan == '1':
            nim = input('Masukkan NIM: ').strip()
            nama = input('Masukkan nama: ').strip()

            q.enqueue(nim,nama)
            print('Mahasiswa berhasil ditambahkan ke antrian.')

        elif pilihan == '2':
            dilayani = q.dequeue()
            print(f'Mahasiswa dilayani: {dilayani.nim} - {dilayani.nama}')

        elif pilihan == '3':
            q.tampilkan()

        elif pilihan == '4':
            print('Program selesai. Terima kasih.')
            break
        else:
            print('Pilihan tidak valid. Silahkan coba lagi.')

    # Penanda eksekusi file utama
if __name__ == '__main__':
    main()