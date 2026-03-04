#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 4 (Memahami kode program Merge Sort)

#==============================

def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid] 
    right = data[mid:] 

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

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

#Jawaban nomor 1: Base case adalah kondisi dalam fungsi rekursif yang menentukan kapan fungsi itu harus berhenti
#Jawaban nomor 2: Karena fungsi rekursif menggunakan looping sehingga ia akan terus memanggil dirinya sendiri sampai ketentuan yang kita tetapkan terpenuhi
#Jawaban nomor 3: Menggabungkan dua kelompok kecil data terurut ke satu kelompok besar data terurut