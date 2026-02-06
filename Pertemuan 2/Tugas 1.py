# ==========================================================
# Tugas 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis file.txt)
# 
# Nama: Dafi Muzaki Wibisono
# NIM: J0403251155
# Kelas: B2
#===========================================================

# Fungsi: Membaca data file

nama_file = "data_barang.txt"

def baca_stok(nama_file):
    stok_dict = {}
    with open(nama_file, 'r', encoding='utf-8') as f: #Membuka dan membaca file
        for baris in f:
            baris = baris.strip() #Untuk menghilangkan \n
            parts = baris.split(',') #Untuk memisahkan kolom
            if len(parts) != 3:
                continue
            kode, nama, stok_str = parts
            stok_int = int(stok_str)
            stok_dict[kode] = {'nama': nama, 'stok': stok_int}

    return stok_dict

# Fungsi: Menyimpan data ke file

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, 'w', encoding='utf-8') as f: # Menulis ulang seluruh isi file berdasarkan stok_dict
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]['nama']
            stok = stok_dict[kode]['stok']
            f.write(f'{kode},{nama},{stok}\n')

# Fungsi: Menampilkan data

def tampilkan_semua(stok_dict):
    if len(stok_dict) == 0: # Jika kosong, tampilkan pesan stok kosong 
        print('Stok kosong.')
        return
    print('\n===== Stok Barang =====')
    print(f"{'Kode': <10} | {'Nama':<12} | {'Stok':>5}") # Tampilkan dengan format rapi: kode | nama | stok 
    print('-' * 30)

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]['nama']
        stok = stok_dict[kode]['stok']
        print(f"{kode:<10} | {nama:<12} | {stok:>5}")

# Fungsi: Cari barang berdasarkan kode

def cari_barang(stok_dict):
    kode_cari = input('Masukkan kode barang yang dicari: ').strip() # Cek apakah kode ada di dictionary 

    if kode_cari in stok_dict: # Jika ada: tampilkan detail barang 
        nama = stok_dict[kode_cari]['nama']
        stok = stok_dict[kode_cari]['stok']
        print('\nBarang ditemukan:')
        print(f"Kode: {kode_cari}")
        print(f"Nama: {nama}")
        print(f"Stok: {stok}")
    else:
        print('Barang dengan kode tersebut tidak ditemukan.') # Jika tidak ada: tampilkan 'Barang tidak ditemukan'

# Fungsi: Tambah barang baru

def tambah_barang(stok_dict): 
    kode = input("Masukkan kode barang baru: ").strip() 

    if kode in stok_dict:
        print('Kode sudah digunakan.')
        return
    
    nama = input("Masukkan nama barang: ").strip()
    try:
        stok_awal = int(input("Masukkan jumlah stok awal: "))
        if stok_awal < 0:
            print("Gagal: Stok tidak boleh negatif!")
            return
    except ValueError:
        print("Gagal: Stok harus berupa angka (integer)!")
        return
    
    stok_dict[kode] = {
        'nama': nama,
        'stok': stok_awal
        }
    
    print(f"Berhasil: Barang '{nama}' telah ditambahkan.")

# Fungsi: Update stok barang

def update_stok(stok_dict): 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() 

    if kode not in stok_dict:
        print("Barang dengan kode tersebut tidak ditemukan.")
        return
    
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 
    
    pilihan = input("Masukkan pilihan (1/2): ").strip()
   
    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        
    except ValueError:
        print("Input harus berupa angka!")
        return
    
    if pilihan == "1":
        stok_dict[kode]['stok'] += jumlah
        print(f"Stok baru ditambahkan!")

    elif pilihan == "2":
        if stok_dict[kode]['stok'] - jumlah < 0:
            print(f"Stok tidak mencukupi!")
        else:
            stok_dict[kode]['stok'] -= jumlah
            print(f"Stok baru dikurangi!")
    
    else:
        print("Pilihan tidak valid!")
 
# Program Utama 

def main():  
    stok_barang = baca_stok(nama_file) # Membaca data dari file saat program mulai
 
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(nama_file, stok_barang) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 

# Menjalankan program utama 

if __name__ == "__main__": 
    main()