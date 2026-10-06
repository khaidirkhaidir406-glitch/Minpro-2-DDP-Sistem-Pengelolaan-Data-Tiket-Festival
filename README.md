# Minpro-2-DDP-Sistem-Pengelolaan-Data-Tiket-Festival

**Nama : Muhammad Khaidir Ali Ramadhani**

**NIM : 2609116015**

**Kelas : A**

Penjelasan Singkat Program : 

Program yang dibuat adalah Sistem Tiket Festival menggunakan bahasa pemrograman Python. Program ini digunakan untuk mengelola data tiket festival seperti kode tiket, nama tiket, kategori tiket, dan harga tiket.

Program memiliki dua jenis akun, yaitu Admin dan User. Sebelum menggunakan program, pengguna harus melakukan login dengan memasukkan username dan password. Jika login berhasil, program akan mengecek jabatan pengguna. Jika pengguna adalah Admin, maka pengguna dapat melihat, menambah, mengubah, dan menghapus data tiket.

Sedangkan jika pengguna adalah User, pengguna hanya dapat melihat data tiket dan melakukan logout.

Program ini dibuat agar pengelolaan data tiket menjadi lebih ``MUDAH``, ``RAPI``, dan ``TERATUR``.


<img width="1417" height="1645" alt="MINPRO-2-DDP-SistemPengelolaanTiketFestival drawio" src="https://github.com/user-attachments/assets/1e59992f-e26f-4dea-b21e-84811f4e3a66" />

# PENJELASAN ALUR FLOWCHART
Alur program dimulai dari Start. Setelah itu program menampilkan judul **SISTEM TIKET FESTIVAL** dan meminta pengguna untuk melakukan login dengan memasukkan username dan password.

Setelah username dan password dimasukkan, program akan mengecek apakah data login tersebut benar atau tidak. Jika username atau password salah, maka program akan menampilkan pesan "Login gagal" dan pengguna diminta untuk mencoba login kembali. Jika username dan password benar, program akan mengecek jabatan pengguna.

# MENU ADMIN

Jika jabatan pengguna adalah ``Admin``, maka pengguna akan masuk ke Menu Admin. Di dalam ``Menu Admin`` terdapat lima pilihan, yaitu ``Tampilkan Data Tiket``, ``Tambah Data Tiket``, ``Ubah Data Tiket``, ``Hapus Data Tiket``, dan ``Logout``.

Jika Admin memilih ``Tampilkan Data Tiket``, program akan menampilkan seluruh data tiket yang tersedia. Jika belum ada data tiket, program akan menampilkan tulisan "Belum ada data tiket yang tersedia."

Jika Admin memilih ``Tambah Data Tiket``, Admin diminta memasukkan nama tiket, kategori tiket, dan harga tiket. Setelah data dimasukkan dengan benar, program akan membuat kode tiket secara otomatis menggunakan angka random. Setelah itu data tiket akan disimpan.

Jika Admin memilih ``Ubah Data Tiket``, Admin memasukkan kode tiket yang ingin diubah. Jika kode tiket ditemukan, program akan menampilkan data tiket tersebut dan Admin dapat memasukkan data yang baru. Jika kode tiket tidak ditemukan, program akan menampilkan pesan "Data tiket tidak ditemukan."

Jika Admin memilih ``Hapus Data Tiket``, Admin memasukkan kode tiket yang ingin dihapus. Program akan menampilkan data tersebut dan meminta konfirmasi terlebih dahulu. Jika Admin memilih "y", data akan dihapus. Jika memilih "n", data tidak jadi dihapus.

Jika Admin memilih ``Logout``, maka Admin keluar dari Menu Admin dan program selesai.

# MENU USER

jika pengguna login sebagai ``User``, maka pengguna masuk ke Menu User. Menu User hanya memiliki dua pilihan, yaitu ``Tampilkan Data Tiket`` dan ``Logout``. User tidak dapat **menambah**, **mengubah**, atau **menghapus data tiket**.

Untuk fungsi dari pilihan menu user, cara kerjanya sama dengan menu admin.

