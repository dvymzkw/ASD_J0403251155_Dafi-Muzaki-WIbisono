#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 3 (Tracing Insertion Sort)

#==============================

def insertion_sort(data):
    print('Data awal: ', data)
    print('='*50)
    
    for i in range(1, len(data)):

        key = data[i] 
        j = i - 1 

        print('Iterasi ke - ', i)
        print('Nilai key = ', i)
        print('Bagian kiri (Terurut): ', data[:i])
        print('Bagian kanan (belum terurut): ', data[i:])
        print('-'*50)

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = key
        print('Setelah disisipkan: ', data)
        print('-'*50)
    return data

angka=[5,2,4,6,1,3]
print('Hasil sorting: ', insertion_sort(angka))

# 1. Membuat kode program Insertion Sort dengan Tracing