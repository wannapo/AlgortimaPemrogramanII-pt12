def selection_sort_ascending(arr):
    # Mengurutkan list (array) menggunakan algoritma Selection Sort secara ascending
    n = len(arr)
    print(f"===== Proses Selection Sort (Ascending) =====")
    print(f"Data Awal: {arr}")

    for i in range(n - 1):
        # Asumsikan elemen pertama dari bagian yang belum terurut adalah yang terkecil
        min_idx = i
        
        print(f"\n--- Iterasi ke-{i+1} ---")
        print(f"Bagian terurut saat ini: {arr[:i]}, Bagian belum terurut: {arr[i:]}")
        print(f"Mencari elemen terkecil dari {arr[i:]} (mulai dari indeks {i})")

        # Cari elemen terkecil di sisa array yang belum terurut
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            print(f" Membandingkan {arr[j]} (indeks {j}) dengan elemen terkecil saat ini ({arr[min_idx]} di indeks {min_idx})")
        
        # Tukar elemen terkecil yang ditemukan dengan elemen pertama dari bagian yang belum terurut
        if min_idx != i:
            print(f" Menemukan elemen terkecil: {arr[min_idx]} di indeks {min_idx}")
            print(f" Menukar {arr[i]} (indeks {i}) dengan {arr[min_idx]} (indeks {min_idx})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i] # Swap
        else:
            print(f" Elemen di indeks {i} ({arr[i]}) sudah yang terkecil di bagian ini. Tidak perlu tukar.")

        print(f"Array setelah iterasi ke-{i+1}: {arr}")

    return arr

# --- Soal Latihan 1: Pengurutan Ascending ---
print("--- Menjalankan Soal Latihan 1 ---")
data_soal1 = [5, 1, 4, 2, 8]
hasil_soal1 = selection_sort_ascending(data_soal1.copy()) # Gunakan .copy()
print(f"\nArray Terurut Akhir (Ascending): {hasil_soal1}")
