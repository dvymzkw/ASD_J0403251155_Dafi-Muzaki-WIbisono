# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus.
# Setiap lokasi menjadi node, sedangkan jalur antar lokasi menjadi edge.
# Bobot pada edge menunjukkan waktu tempuh dalam satuan menit.
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari satu lokasi awal
    ke semua lokasi lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari lokasi awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak sementara, nama lokasi).
    # Lokasi dengan jarak terkecil akan diproses lebih dulu.
    priority_queue = [(0, start)]

    # Proses berjalan selama masih ada lokasi yang perlu diperiksa.
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari jarak terbaik saat ini,
        # data tersebut dilewati karena sudah ada jalur yang lebih pendek.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari lokasi saat ini.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih pendek, update jaraknya
            # lalu masukkan kembali ke priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma Dijkstra dari lokasi awal Gerbang.
hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Lokasi yang paling dekat dari Gerbang adalah Kantin,
#    karena jarak terpendeknya hanya 2 menit.
#
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit,
#    melalui jalur Gerbang -> Kantin -> Lab -> Aula.
#
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu. Jalur langsung bisa saja memiliki bobot lebih besar
#    dibandingkan jalur tidak langsung yang melewati beberapa lokasi lain.
#    Pada kasus ini, jalur Gerbang -> Kantin -> Aula membutuhkan 9 menit,
#    sedangkan Gerbang -> Kantin -> Lab -> Aula hanya membutuhkan 7 menit.
#
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Dijkstra cocok digunakan karena semua bobot waktu tempuh bernilai positif.
#    Algoritma ini efisien untuk mencari jarak terpendek dari satu lokasi awal
#    ke banyak lokasi tujuan pada graph berbobot positif.
