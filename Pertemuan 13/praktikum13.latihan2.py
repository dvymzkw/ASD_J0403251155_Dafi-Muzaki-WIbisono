# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Latihan 2
# ========================================================== 

import heapq

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = [] 
total_weight = 0 

connected = set() 

for weight, u, v in edges: 
    
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 
        
        mst.append((u, v, weight)) 
        total_weight += weight 
        
        connected.add(u) 
        connected.add(v) 
        
print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 
            
print("Total bobot =", total_weight) 

# Jawaban Analisis: 
# 1. Edge mana yang dipilih pertama kali? 
#    Edge pertama yang dipilih adalah (1, 'C', 'D') karena memiliki 
#    bobot paling kecil (1) di antara semua edge yang ada.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
#    Karena prinsip algoritma MST adalah mencari solusi optimal lokal 
#    pada setiap langkah untuk memastikan biaya total akhir 
#    adalah yang paling minimum (efisiensi biaya).
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 1 + 2 + 3 = 6. 
#    (Terdiri dari edge C-D=1, A-C=2, dan B-D=3).
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge (4, 'A', 'B') dan (5, 'A', 'D') tidak dipilih karena node-node 
#    tersebut (A, B, C, D) sudah terhubung ke dalam MST melalui jalur yang 
#    lebih murah. Menambahkan edge tersebut hanya akan menciptakan 
#    redundansi jalur atau siklus, yang tidak diperbolehkan dalam pohon (tree).