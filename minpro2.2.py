print("=== Sistem Reservasi Hotel ===")

users = {
    "polisi bulan sabit": {"password": "kauyangkuasaibumikh", "role": "admin"},
    "pelanggan baru": {"password": "apaya", "role": "customer"},
    "langganan": {"password": "apasi", "role": "customer"}
}

reservasi = {}

def tampilkan_menu_admin():
    print("\nMenu Admin:")
    print("1. Tambah Reservasi")
    print("2. Update Reservasi")
    print("3. Hapus Reservasi")
    print("4. Lihat Semua Reservasi")
    print("5. Keluar")

def tampilkan_menu_customer():
    print("\nMenu Customer:")
    print("1. Tambah Reservasi")
    print("2. Lihat Reservasi Saya")
    print("3. Keluar")

def pilih_kamar():
    print("Jenis kamar yang tersedia:")
    print("1. Kamar Standard - Rp 500.000 per malam")
    print("2. Kamar Deluxe   - Rp 800.000 per malam")
    print("3. Kamar Suite    - Rp 1.200.000 per malam")
    kamar_pilihan = input("Masukkan nomor jenis kamar (1/2/3): ")
    if kamar_pilihan == "1":
        return "Standard", 500000
    elif kamar_pilihan == "2":
        return "Deluxe", 800000
    elif kamar_pilihan == "3":
        return "Suite", 1200000
    else:
        print("Pilihan kamar tidak tersedia.")
        return None, 0

def input_lama_menginap():
    lama = input("Masukkan lama menginap (malam): ")
    if lama.isdigit():
        lama = int(lama)
        if lama > 0:
            return lama
    print("Input lama menginap tidak valid.")
    return None

while True:
    try:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if not password.isalpha():
            raise ValueError

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nLogin berhasil! Anda masuk sebagai {role}.")
            break
        else:
            print("Login gagal. Coba lagi.\n")

    except ValueError:
        print("Error: Password hanya boleh huruf (a-z).\n")

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna (Ctrl + C).")
        exit()

while True:
    try:
        if role == "admin":
            tampilkan_menu_admin()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                nama = input("Masukkan nama tamu: ")
                if nama in reservasi:
                    print("Nama sudah terdaftar, gunakan nama lain.")
                else:
                    kamar, harga = pilih_kamar()
                    if kamar == None: 
                        continue
                    lama = input_lama_menginap()
                    if lama == None: 
                        continue
                    total = harga * lama
                    reservasi[nama] = {"kamar": kamar, "lama": lama, "total": total}
                    print(f"Reservasi untuk {nama} berhasil ditambahkan.")

            elif pilihan == "2":
                nama = input("Masukkan nama tamu yang ingin diupdate: ")
                if nama in reservasi:
                    kamar, harga = pilih_kamar()
                    if kamar == None: 
                        continue
                    lama = input_lama_menginap()
                    if lama == None: 
                        continue
                    total = harga * lama
                    reservasi[nama] = {"kamar": kamar, "lama": lama, "total": total}
                    print(f"Reservasi untuk {nama} berhasil diupdate.")
                else:
                    print("Reservasi tidak ditemukan.")

            elif pilihan == "3":
                nama = input("Masukkan nama tamu yang ingin dihapus: ")
                if nama in reservasi:
                    del reservasi[nama]
                    print(f"Reservasi untuk {nama} berhasil dihapus.")
                else:
                    print("Reservasi tidak ditemukan.")

            elif pilihan == "4":
                if len(reservasi) == 0:
                    print("Belum ada reservasi.")
                else:
                    print("\nDaftar Reservasi:")
                    for nama, data in reservasi.items():
                        print(f"- {nama}: Kamar {data['kamar']}, {data['lama']} malam, Total Rp {data['total']:,}")

            elif pilihan == "5":
                print("Keluar dari sistem. Terima kasih.")
                break
            else:
                print("Pilihan tidak valid.")

        elif role == "customer":
            tampilkan_menu_customer()
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                if username in reservasi:
                    print("Anda sudah memiliki reservasi. Tidak bisa menambah lagi.")
                else:
                    kamar, harga = pilih_kamar()
                    if kamar == None: 
                        continue
                    lama = input_lama_menginap()
                    if lama == None: 
                        continue
                    total = harga * lama
                    reservasi[username] = {"kamar": kamar, "lama": lama, "total": total}
                    print(f"Reservasi berhasil ditambahkan atas nama {username}.")

            elif pilihan == "2":
                if username in reservasi:
                    data = reservasi[username]
                    print(f"Reservasi Anda: Kamar {data['kamar']}, {data['lama']} malam, Total Rp {data['total']:,}")
                else:
                    print("Anda belum memiliki reservasi.")

            elif pilihan == "3":
                print("Keluar dari sistem. Terima kasih.")
                break
            else:
                print("Pilihan tidak valid.")

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna (Ctrl + C).")
        exit()


