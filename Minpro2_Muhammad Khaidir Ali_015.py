import pwinput
import random
import os

akun = {
    "admin": {
        "password": "AcenkPilek",
        "Jabatan": "Admin",
    },
    "user": {
        "password": "Kacunk123",
        "Jabatan": "User"
    }
}


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

    
data_tiket = {
    "T001": {
        "nama": "Rakyat Pass",
        "kategori": "Regular",
        "harga": 100000,
    },
    "T002": {
        "nama": "Raja Pass",
        "kategori": "Premium",
        "harga": 200000,
    }
}


def login():
    print("=" * 30)
    print("LOGIN DULU LEE")
    print("=" * 30)

    while True:
        username = input("Username: ").lower()
        password = pwinput.pwinput("Password: ")

        if username in akun and akun[username]["password"] == password:
            print("\nCOCOKKKK!")
            print("Welkam braderr,", username)
            return akun[username]["Jabatan"].lower()

        print("LAU SIAPE MPRUYY???")
        print("Coba lagi brayy.\n")


def tampilkan_data():
    print("=" * 30)
    print("DATA TIKET FESTIVAL")
    print("=" * 30)

    if len(data_tiket) == 0:
        print("Belum ada data tiket yang tersedia.")
    else:
        for kode, tiket in data_tiket.items():
            print("Kode     :", kode)
            print("Nama     :", tiket["nama"])
            print("Kategori :", tiket["kategori"])
            print("Harga    : Rp.", format(tiket["harga"], ",").replace(",", "."))
            print("-" * 30)



def buat_kode():
    while True:
        angka = random.randint(100, 999)
        kode = "T" + str(angka)

        if kode not in data_tiket:
            return kode


def tambah_data():
    print("=" * 30)
    print("TAMBAH DATA TIKET")
    print("=" * 30)

    nama = input("Nama tiket      : ")
    kategori = input("Kategori tiket  : ")

    try:
        harga = int(input("Harga tiket (Rp): "))

        if harga <= 0:
            print("Harga tiket harus lebih dari 0.")
            return

        kode = buat_kode()

        data_tiket[kode] = {
            "nama": nama,
            "kategori": kategori,
            "harga": harga
        }

        print("\nData tiket berhasil ditambahkan.")
        print("Kode tiket:", kode)

    except ValueError:
        print("Harga tiket harus berupa angka.")


def ubah_data():
    print("=" * 30)
    print("UBAH DATA TIKET")
    print("=" * 30)

    kode = input("Masukkan kode tiket: ").upper()

    if kode in data_tiket:
        print("\nData ada nih brayy!")
        print("Nama     :", data_tiket[kode]["nama"])
        print("Kategori :", data_tiket[kode]["kategori"])
        print("Harga    :", data_tiket[kode]["harga"])

        print("\nMasukkan data baru:")
        nama = input("Nama tiket      : ")
        kategori = input("Kategori tiket  : ")

        try:
            harga = int(input("Harga tiket (Rp): "))

            if harga <= 0:
                print("Harga tiket harus lebih dari 0.")
                return

            data_tiket[kode]["nama"] = nama
            data_tiket[kode]["kategori"] = kategori
            data_tiket[kode]["harga"] = harga

            print("\nData tiket berhasil diubah.")

        except ValueError:
            print("Harga tiket harus berupa angka.")

    else:
        print("\nData tiket tidak ditemukan.")


def hapus_data():
    print("=" * 30)
    print("HAPUS DATA TIKET")
    print("=" * 30)

    kode = input("Masukkan kode tiket: ").upper()

    if kode in data_tiket:
        print("\nData yang akan dihapus:")
        print("Nama:", data_tiket[kode]["nama"])

        konfirmasi = input(
            "EH beneran pengen dihapus kah? (y/n): "
        ).lower()

        if konfirmasi == "y":
            del data_tiket[kode]
            print("\nData tiket berhasil dihapus.")
        else:
            print("\nPenghapusan data dibatalkan.")

    else:
        print("\nData tiket tidak ditemukan.")



def menu_admin():
    while True:
        print("=" * 30)
        print("MENU ADMIN")
        print("=" * 30)

        print("1. Tampilkan Data Tiket")
        print("2. Tambah Data Tiket")
        print("3. Ubah Data Tiket")
        print("4. Hapus Data Tiket")
        print("5. Logout")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


def menu_user():
    while True:
        print("=" * 30)
        print("MENU USER")
        print("=" * 30)

        print("1. Tampilkan Data Tiket")
        print("2. Logout")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")



print("=" * 30)
print("SISTEM TIKET FESTIVAL")
print("=" * 30)

role = login()

if role == "admin":
    menu_admin()
elif role == "user":
    menu_user()

bersihkan_layar()
print("\nTHANKSS BRAAYYYY")

