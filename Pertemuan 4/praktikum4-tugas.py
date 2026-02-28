#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None

class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None

    # Menambahkan data baru ke bagian belakang (rear) => menambahkan antrian pelanggan yang ingin memperbaiki motor
    def enqueue(self, no, nama, servis):
        # Jika data baru masuk dari queue yang kosong maka data baru = front = rear
        nodeBaru = Node(no,nama,servis)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong, maka data baru diletakkan stelah rear kemudian dijadikan sebagai rear 
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # Menghapus data paling depan (memberikan layanan bengkel)
    def dequeue(self):
        if self.is_empty():
            print('Antrian kosong. Tidak ada pelanggan yang dilayani.')
            return None

        # Lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        # Menggeser pointer front ke next front
        self.front = self.front.next

        # Jika front menjadi none (data terakhir pelanggan yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilkan(self):
        print('Daftar antrian pelanggan (front -> rear)')
        current = self.front
        while current is not None:
            print(f"{current.no}. {current.nama} - {current.servis}")
            current = current.next

# Main Menu

def main():

    #Instantiasi queue
    q = QueueBengkel()

    while True:
        print('=== Sistem Antrian Bengkel ===')
        print('1. Tambah Pelanggan')
        print('2. Layani Pelanggan')
        print('3. Lihat Antrian')
        print('4. Keluar')

        pilihan = input('Pilih menu (1-4): ').strip()

        if pilihan == '1':
            no = input('Masukkan nomor: ').strip()
            nama = input('Masukkan nama: ').strip()
            servis = input('Masukkan jenis servis: ').strip()

            q.enqueue(no,nama,servis)
            print('Pelanggan berhasil ditambahkan ke antrian.')

        elif pilihan == '2':
            dilayani = q.dequeue()
            print(f'Pelanggan dilayani: {dilayani.no} - {dilayani.nama} - {dilayani.servis}')

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