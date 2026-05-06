# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 5: Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq


# Graph berbobot yang merepresentasikan hubungan antar kota.
# Formatnya: 'kota_asal': {'kota_tujuan': bobot_jarak}
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari satu kota awal
    ke semua kota lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari kota awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak sementara, nama kota).
    # Kota dengan jarak paling kecil akan diproses terlebih dahulu.
    priority_queue = [(0, start)]

    # Proses berjalan selama masih ada kota yang perlu diperiksa.
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari jarak terbaik saat ini,
        # data tersebut dilewati karena sudah ada jalur yang lebih pendek.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota tetangga dari kota yang sedang diproses.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih pendek,
            # simpan jarak baru tersebut dan masukkan ke priority queue.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menentukan node awal pencarian jalur terpendek.
node_awal = 'Bogor'

# Menjalankan algoritma Dijkstra dari node awal.
hasil = dijkstra(graph, node_awal)

print("Jarak terpendek dari", node_awal, "ke semua kota:")
for kota, jarak in hasil.items():
    print(kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah Bogor.
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Node yang memiliki jarak paling kecil dari Bogor adalah Depok,
#    dengan jarak terpendek 2.
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Node yang memiliki jarak paling besar dari Bogor adalah Bandung,
#    dengan jarak terpendek 8.
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Algoritma Dijkstra dimulai dari Bogor dengan jarak 0.
#    Setelah itu, algoritma memeriksa kota tetangga Bogor, yaitu Jakarta
#    dan Depok. Depok diproses lebih dulu karena jaraknya lebih kecil,
#    yaitu 2. Dari Depok, ditemukan jalur ke Jakarta dengan total jarak 4
#    dan jalur ke Bandung dengan total jarak 8. Jarak Jakarta diperbarui
#    dari 5 menjadi 4 karena jalur Bogor -> Depok -> Jakarta lebih pendek.
#    Hasil akhirnya adalah Bogor = 0, Depok = 2, Jakarta = 4,
#    dan Bandung = 8.
