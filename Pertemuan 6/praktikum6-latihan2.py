#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 2 (Melengkapi potongan kode)

#==============================

def insertion_sort_ascending(data):
    for i in range(1, len(data)):
        key = data[i] 
        j = i - 1

        while j >= 0 and data[j] > key: 
            data[j+1] = data[j] 
            j-=1

        data[j+1] = key
    return data

def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i] 
        j = i - 1

        while j >= 0 and data[j] < key: 
            data[j+1] = data[j] 
            j-=1

        data[j+1] = key
    return data


angka = [7,8,5,2,4,6]
print('Hasil sorting (ascending): ', insertion_sort_ascending(angka))
print('Hasil sorting (descending): ', insertion_sort_descending(angka))

# 1. Melengkapi kode ascending: Menambahkan "data[j] > key" dan "data[j+1] = key"
# 2. Membuat kode program descending