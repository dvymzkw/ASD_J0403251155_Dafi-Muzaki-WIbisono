#============================================
# Praktikum 1: Konsep ADT & File Handling
#============================================

# Membuka file dengan mode read ("r")

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    isi_file = file.read() # Membaca file
print(isi_file)

print('===Hasil Read===')
print('Tipe Data:', type(isi_file))
print('Jumlah Karakter:', len(isi_file))
print('Jumlah Baris:', isi_file.count('\n')+1)

#=============================================

# Membuka file per baris

print('===Membaca file per baris===')
jumlah_baris=0
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris=jumlah_baris+1
        baris=baris.strip()
        print('Baris ke -', jumlah_baris)
        print('Isinya: ', baris)

#=============================================

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris=baris.strip()
        nim, nama, nilai = baris.split(',') # Parsing data karakter
        print('NIM:', nim, 'Nama:', nama, 'Nilai:', nilai)

#=============================================

data_list=[] # List untuk menampung data mahasiswa

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris=baris.strip()
        nim, nama, nilai=baris.split(',')
        # Simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print('=== Data mahasiswa dalam list')
print(data_list)

print('=== Jumlah record dalam list')
print('Jumlah record', len(data_list))

print('=== Menampilkan data record tertentu ===')
print('Contoh record pertama: ', data_list[0])

#============================================

data_dict={} # Buat variable untuk dictionary

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris=baris.strip()
        nim, nama, nilai=baris.split(',')

        # Simpan data mahasiswa  ke dictionary
        data_dict[nim] = {
            'nama': nama,
            'nilai': int(nilai)
        }
print('=== Data mahasiswa dalam dictionary ===')
print(data_dict)