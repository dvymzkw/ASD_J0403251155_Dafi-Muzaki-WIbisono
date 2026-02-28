#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Materi Rekursif: Menjumlahkan Elemen List

#==============================

def jumlah_list(data,index=0):
    #Base case
    if index == len(data):
        return 0

    return data[index] + jumlah_list(data,index+1)
print('=== Program Jumlah Data ===')
print(jumlah_list([2,3,4,5,6]))