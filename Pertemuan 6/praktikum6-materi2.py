#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Insertion Sort dengan Tracing

#==============================

def insertion_sort(data):
    #Loop mulai dari data le 2 (index array ke 1)
    
    #Melihat data awal
    print('Data awal: ', data)
    print('='*50)
    
    for i in range(1, len(data)):

        key = data[i] #Simpan nilai yang disisipkan
        j = i - 1 #Index elemen terakhir di bagian kiri

        print('Iterasi ke - ', i)
        print('Nilai key = ', i)
        print('Bagian kiri (Terurut): ', data[:i])
        print('Bagian kanan (belum terurut): ', data[i:])
        print('-'*50)

        #Geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        #Sisipkan key ke posisi yang benar
        data[j+1] = key
        print('Setelah disisipkan: ', data)
        print('-'*50)
    return data

angka=[7,8,5,2,4,6]
print('Hasil sorting: ', insertion_sort(angka))