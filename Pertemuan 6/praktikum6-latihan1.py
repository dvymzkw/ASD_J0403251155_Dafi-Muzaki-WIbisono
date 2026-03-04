#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 1 (Memahami kode program Insertion Sort)

#==============================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i] 
        j = i - 1

        while j >= 0 and data[j] > key: 
            data[j+1] = data[j] 
            j-=1

        data[j+1] = key
    return data

# Jawaban soal 1: Karena index 0 sudah dianggap bagian yang terurut
# Jawaban soal 2: variable key berfungsi untuk menyimpan nilai yang akan disisipkan di urutan yang benar
# Jawaban soal 3: Karena kita tidak tahu pasti ada berapa banyak elemen yang harus digeser
# Jawaban soal 4: Elemen yang lebih besar dari key akan dipindahkan ke sebelah kanan, dan j akan terus berkurang untuk memeriksa elemen sebelumnya (sampai awal array) sudah sesuai atau belum