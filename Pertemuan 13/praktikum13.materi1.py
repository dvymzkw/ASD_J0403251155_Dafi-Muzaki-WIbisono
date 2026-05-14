# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Implementasi Kruskal 
# ========================================================== 

# Daftar edge: (bobot, node1, node2) 
edges = [ (1, 'C', 'D'),
          (2, 'A', 'C'),
          (3, 'B', 'D'), 
          (4, 'A', 'B'), 
          (5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot dari yang paling kecil
# agar edge dengan biaya terendah diproses lebih dulu.
edges.sort()  

# Menyimpan edge-edge yang masuk ke Minimum Spanning Tree.
mst = [] 

# Menyimpan jumlah seluruh bobot edge yang terpilih.
total_weight = 0  

# Set sederhana untuk node yang sudah dipilih 
connected = set()  

# Memeriksa setiap edge yang sudah diurutkan berdasarkan bobot.
for weight, u, v in edges:      

    # Jika salah satu node belum terhubung, edge dipilih
    # karena dianggap tidak membentuk cycle sederhana.
    if u not in connected or v not in connected:          

        # Menambahkan edge ke dalam MST.
        mst.append((u, v, weight))         

        # Menambahkan bobot edge ke total bobot MST.
        total_weight += weight          

        # Menandai kedua node sebagai node yang sudah terhubung.
        connected.add(u)         
        connected.add(v)  
        
print("Minimum Spanning Tree:")  

# Menampilkan semua edge yang terpilih sebagai MST.
for edge in mst:     
    print(edge)  
            
# Menampilkan total bobot dari MST.
print("Total bobot =", total_weight)
