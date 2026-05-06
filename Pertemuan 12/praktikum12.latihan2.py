# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif.
# Dijkstra cocok digunakan jika semua bobot edge tidak negatif.
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak sementara, node).
    # Node dengan jarak terkecil akan diproses lebih dahulu.
    priority_queue = [(0, start)]

    # Proses dilakukan selama masih ada node di priority queue.
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati karena sudah ada jalur yang lebih pendek.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma Dijkstra dari node A.
hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
#    Jarak terpendek dari A ke B adalah 4.
#
# 2. Berapa jarak terpendek dari A ke C?
#    Jarak terpendek dari A ke C adalah 2.
#
# 3. Berapa jarak terpendek dari A ke D?
#    Jarak terpendek dari A ke D adalah 3.
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Karena jalur A -> C -> D memiliki total bobot 3,
#    sedangkan jalur A -> B -> D memiliki total bobot 9.
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Priority queue berfungsi memilih node dengan jarak sementara paling kecil
#    agar node tersebut diproses lebih dahulu.
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Karena Dijkstra menganggap jarak terkecil yang sudah diproses tidak perlu
#    diperbaiki lagi. Bobot negatif dapat membuat asumsi tersebut salah.
