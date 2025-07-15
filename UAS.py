# Meminta jumlah customer
nama_customer = int(input("Masukkan nama customer: "))

# Dictionary untuk menyimpan nama customer
harga_barang = {}

# Menginput data untuk setiap customer
for i in range(harga_barang):
    print(f"\nMasukkan nama customer-{i+1}:")
    Tanggal_belanja = input("  Masukkan tanggal belanja (YYYY-MM-DD): ")
    Jumlah_Barang = input("  Masukkan Jumlah barang: ")
    
    jumlah_barang = int(input("  Masukkan jumlah barang: "))
    nilai_barang = []

    for j in range(jumlah_barang):
        nb = input(f"    Nama barang ke-{j+1}: ")
        harga_satuan_barang = float(input(f"    Harga satuan barang {nb}: "))
        nilai_nb.append((nb, harga_satuan_barang))
    
    data_customer[taggal_belanja] = {
        "nama": nama,
        "jumlah_barang": jumlah_barang
    }

# Menampilkan semua data customer
print("\nData Customer dan jumlah barang:")
for nim, info in data_customer.items():
    nama = info["nama"]
    nama_barang = info["nama_barang"]
    jumlah_barang = sum([jumlah_barang for _, jumlah_barang in nama_barang]) / len(nama_barang)
    
    print(f"\ntanggal_belanja: {tanggal_belanja}")
    print(f"Nama: {nama}")
    print("Jumlah_barang dan Nama_barang:")
    for nb, jumlah_barang in nama_barang:
        print(f"  - {nb}: {nama_barang}")
    print(f"nama barang: {rata_barang:.2f}")