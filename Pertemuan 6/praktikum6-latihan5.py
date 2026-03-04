#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 5 (Melengkapi fungsi Merge Sort)

#==============================

def merge(left,right):
    result = []
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 1. Melengkapi kode program ascending: Menambahkan "left[i] <= right[j]"
# 2. Fungsi result.extend() adalah menambahkan sisa elemen yang ada di list kanan/kiri