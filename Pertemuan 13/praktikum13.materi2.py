# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Implementasi Prim
# ========================================================== 

# Modul heapq digunakan untuk membuat priority queue,
# sehingga edge dengan bobot terkecil dapat diambil lebih dulu.
import heapq  

# Representasi graph menggunakan adjacency list.
# Setiap node menyimpan tetangga dan bobot edge-nya.
graph = {     
    'A': {'B': 4, 'C': 2, 'D': 5},     
    'B': {'A': 4, 'D': 3},     
    'C': {'A': 2, 'D': 1},     
    'D': {'A': 5, 'B': 3, 'C': 1} }  

# Fungsi untuk mencari Minimum Spanning Tree menggunakan algoritma Prim.
def prim(graph, start):      
    
    # Set untuk menyimpan node yang sudah masuk ke MST.
    visited = set([start])      
    
    # Priority queue untuk menyimpan kandidat edge.
    edges = []      
    
    # Memasukkan semua edge dari node awal ke priority queue.
    for neighbor, weight in graph[start].items():         
        heapq.heappush(edges, (weight, start, neighbor))      
        
        # Menyimpan edge yang terpilih sebagai bagian dari MST.
        mst = []     

        # Menyimpan total bobot semua edge pada MST.
        total_weight = 0      
        
        # Selama masih ada edge kandidat, ambil edge dengan bobot terkecil.
        while edges:          
        
            weight, u, v = heapq.heappop(edges)          
        
            # Edge dipilih hanya jika node tujuan belum dikunjungi.
            if v not in visited:              
        
                # Menandai node tujuan sebagai node yang sudah masuk MST.
                visited.add(v)              
        
                # Menambahkan edge terpilih ke MST dan menjumlahkan bobotnya.
                mst.append((u, v, weight))             
                total_weight += weight              
        
                # Memasukkan edge dari node baru ke priority queue
                # jika tetangganya belum dikunjungi.
                for neighbor, w in graph[v].items():                  
        
                    if neighbor not in visited:                     
                        heapq.heappush(edges, (w, v, neighbor))      
        
        # Mengembalikan daftar edge MST dan total bobotnya.
        return mst, total_weight   

# Menjalankan algoritma Prim mulai dari node A.
mst, total = prim(graph, 'A')  

print("Minimum Spanning Tree:")  

# Menampilkan edge-edge yang terpilih sebagai MST.
for edge in mst:     
    print(edge)  
                        
# Menampilkan total bobot dari MST.
print("Total bobot =", total) 
