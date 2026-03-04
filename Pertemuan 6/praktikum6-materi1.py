#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Insertion Sort (Ascending)

#==============================

def insertion_sort(data):
    #Loop mulai dari data le 2 (index array ke 1)
    for i in range(1, len(data)):
        key = data[i] #Simpan nilai yang disisipkan
        j = i - 1 #Index elemen terakhir di bagian kiri

        #Geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j-=1

        #Sisipkan key ke posisi yang benar
        data[j+1] = key
    return data

angka = [7,8,5,2,4,6]
print('Hasil sorting: ', insertion_sort(angka))