# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Latihan 3
# ========================================================== 

import heapq

graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start): 
    
    visited = set([start]) 
    edges = [] 
    
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    
    mst = [] 
    total_weight = 0 
        
    while edges: 
        weight, u, v = heapq.heappop(edges) 
        
        if v not in visited: 
            
            visited.add(v) 
            
            mst.append((u, v, weight)) 
            total_weight += weight 
            
            for neighbor, w in graph[v].items(): 
                
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
                    
    return mst, total_weight 

mst, total = prim(graph, 'A') 

print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 
    
print("Total bobot =", total) 

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge ('A', 'C') dengan bobot 2, karena merupakan edge dengan bobot 
#    terkecil yang terhubung langsung ke node 'A'.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim selalu memilih edge dengan bobot terkecil yang menghubungkan 
#    salah satu node di dalam 'visited set' (sudah terpilih) ke node yang 
#    berada di luar 'visited set' (belum terpilih), sehingga tidak membentuk siklus.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 6 (terdiri dari edge A-C: 2, C-D: 1, dan D-B: 3).
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Prim: Membangun MST dengan mengembangkan pohon dari satu node awal 
#      secara bertahap.
#    - Kruskal: Membangun MST dengan menyatukan edge-edge paling murah 
#      di seluruh graf tanpa mempedulikan apakah edge tersebut terhubung 
#      dengan pohon yang sedang dibentuk atau tidak, selama tidak membentuk siklus.

