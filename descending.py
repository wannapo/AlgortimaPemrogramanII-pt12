def selection_sort_descending(arr):
    # Mengurutkan list (array) menggunakan algoritma Selection Sort secara descending
    n = len(arr)
    print(f"===== Proses Selection Sort (Descending) =====")
    print(f"Data Awal: {arr}")

    for i in range(n - 1):
        # Asumsikan elemen pertama dari bagian yang belum terurut adalah yang terbesar
        max_idx = i
        
        print(f"\n--- Iterasi ke-{i+1} ---")
        print(f"Bagian terurut saat ini: {arr[:i]}, Bagian belum terurut: {arr[i:]}")
        print(f"Mencari elemen terbesar dari {arr[i:]} (mulai dari indeks {i})")

        # Cari elemen terbesar di sisa array yang belum terurut
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]: # Perubahan di sini: arr[j] > arr[max_idx]
                max_idx = j
            print(f" Membandingkan {arr[j]} (indeks {j}) dengan elemen terbesar saat ini ({arr[max_idx]} di indeks {max_idx})")
        
        # Tukar elemen terbesar yang ditemukan dengan elemen pertama dari bagian yang belum terurut
        if max_idx != i:
            print(f" Menemukan elemen terbesar: {arr[max_idx]} di indeks {max_idx}")
            print(f" Menukar {arr[i]} (indeks {i}) dengan {arr[max_idx]} (indeks {max_idx})")
            arr[i], max_idx = arr[max_idx], arr[i] # Swap
            # Catatan: Di modul tertulis arr[i], arr[max_idx] = arr[max_idx], arr[i]
            arr[i], arr[max_idx] = arr[max_idx], arr[i] 
        else:
            print(f" Elemen di indeks {i} ({arr[i]}) sudah yang terbesar di bagian ini. Tidak perlu tukar.")

        print(f"Array setelah iterasi ke-{i+1}: {arr}")

    return arr

# --- Soal Latihan 2: Pengurutan Descending ---
print("--- Menjalankan Soal Latihan 2 ---")
data_soal2 = [10, 5, 8, 20, 15]
hasil_soal2 = selection_sort_descending(data_soal2.copy()) # Gunakan .copy()
print(f"\nArray Terurut Akhir (Descending): {hasil_soal2}")
