# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Latihan 4
# ========================================================== 

import heapq

# Representasi weighted graph menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Menyimpan node yang sudah dikunjungi (dalam pohon)
    visited = set([start])
    # Priority queue untuk menyimpan edge (bobot, node_asal, node_tujuan)
    edges = []
    
    # Inisialisasi: masukkan semua tetangga dari node awal ke antrian
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    
    mst = []
    total_weight = 0
        
    # Proses membangun pohon
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan belum dikunjungi, tambahkan ke MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan tetangga dari node baru ke antrian
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

# Menjalankan program dimulai dari Gedung A
start_node = 'A'
mst, total = prim(graph, start_node)

print("--- Hasil Jaringan Kabel Biaya Minimum (MST) ---")
print("Edge yang dipilih:")
for edge in mst:
    print(f"Gedung {edge[0]} - Gedung {edge[1]} (Biaya: {edge[2]})")
    
print(f"\nTotal biaya minimum = {total}")

"""
PENJELASAN PROGRAM:
1. Representasi Graf: Menggunakan dictionary of dictionaries agar mudah 
   mengakses hubungan gedung dan bobot (biaya) kabelnya.
2. Algoritma Prim: Memulai dari satu titik ('A'), lalu secara greedy 
   selalu memilih edge dengan bobot terkecil yang menghubungkan 
   gedung baru ke jaringan yang sudah ada.
3. Priority Queue: Menggunakan heapq untuk memastikan kita selalu 
   mengambil edge dengan bobot paling murah di antara pilihan yang ada.
4. Efisiensi: Program memastikan semua gedung terhubung tanpa 
   membentuk siklus yang tidak perlu, sehingga biaya totalnya minimal.
"""

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma yang digunakan adalah Algoritma Prim. Algoritma ini 
#    bekerja dengan cara memulai dari satu simpul (node) awal dan 
#    secara bertahap menambahkan edge dengan bobot terkecil yang 
#    menghubungkan simpul di dalam pohon ke simpul di luar pohon.
#
# 2. Edge mana saja yang dipilih?
#    Berdasarkan hasil eksekusi algoritma, edge yang dipilih adalah:
#    - Gedung A - Gedung C (Biaya: 2)
#    - Gedung C - Gedung D (Biaya: 1)
#    - Gedung D - Gedung B (Biaya: 3)
#
# 3. Berapa total biaya minimum?
#    Total biaya minimum adalah 2 + 1 + 3 = 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST (Minimum Spanning Tree) sangat cocok karena tujuan utamanya 
#    adalah menghubungkan semua simpul (gedung) dalam graf dengan 
#    jumlah edge (kabel) seminimal mungkin dan total bobot (biaya) 
#    yang paling rendah. Pada kasus infrastruktur fisik seperti 
#    pemasangan kabel, efisiensi biaya adalah prioritas utama, 
#    dan MST memberikan solusi matematis yang optimal untuk itu.