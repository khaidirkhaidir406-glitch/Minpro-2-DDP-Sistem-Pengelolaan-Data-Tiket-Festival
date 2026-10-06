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

# DOKUMENTASI PROGRAM & OUTPUT

**MENU ADMIN**

<img width="264" height="198" alt="Screenshot 2026-10-06 212145" src="https://github.com/user-attachments/assets/d8fd30fb-b959-4244-9380-8a174e267d5f" />

Bagian ini ditemukan pada awal program ini ditemukan, digunakan untuk meminta pengguna melakukan login terlebih dahulu.


<img width="258" height="272" alt="Screenshot 2026-10-06 212545" src="https://github.com/user-attachments/assets/32baff80-f768-4243-b3e2-9d0979d0e93b" />

Bagian ini ditemukan setelah kita memasukkan ``username`` dan ``password`` yang benar, jika username dan password sesuai dengan kode admin, maka program akan menampilkan menu admin.

<img width="282" height="228" alt="Screenshot 2026-10-06 215108" src="https://github.com/user-attachments/assets/71106294-15a1-4e24-9ee4-7298a5e5a723" />

Ini adalah suatu kondisi dimana kita tidak sesuai dalam memasukkan password. program akan otomatis meminta kita untuk memasukkan username dan password kembali.


**MENAMPILKAN DATA TIKET**

<img width="266" height="390" alt="Screenshot 2026-10-06 212920" src="https://github.com/user-attachments/assets/edcf3a64-67c4-4fe6-bf70-34300cca85bc" />

Bagian ini ditemukan jika kita memilih pilihan 1, dimana pilihan ini akan menampilkan data tiket yang tersedia. Data tersebut berasal dari ``data_tiket`` yang sudah dibuat di dalam program.

**MENAMBAH DATA TIKET**

<img width="289" height="330" alt="Screenshot 2026-10-06 213322" src="https://github.com/user-attachments/assets/66f512f0-c47b-4af0-af19-368a74717f5e" />

Bagian in ditemukan jika kita memilih pilihan 2, dimana pilihan ini digunakan untuk memasukkan/menambah data tiket ke dalam sistem program kita.

<img width="314" height="449" alt="Screenshot 2026-10-06 215158" src="https://github.com/user-attachments/assets/93d14ee8-c9fa-4247-9d7f-8dfdcc86a642" />

Bagian ini ditemukan jika kita memasukkan data harga tiket tidak menggunakan bilangan/int


**MENGUBAH DATA TIKET**

<img width="274" height="449" alt="Screenshot 2026-10-06 213617" src="https://github.com/user-attachments/assets/43bb34b4-bf2e-48c8-9c74-4854b91c9695" />

Bagian ini ditemukan jika kita memilih pilihan 3, dimana kita ingin mengubah suatu data tiket menjadi sebuah data tiket yang baru, dengan cara mengetik kode tiket yang telah kita dapatkan secara otomatis setelah menambah data tiket sebelumnya.

<img width="268" height="279" alt="Screenshot 2026-10-06 213649" src="https://github.com/user-attachments/assets/df3577f6-0a88-45f1-85eb-9c95086d3ede" />

Namun, jika kode tiket tidak sesuai dengan kode tiket yang dimiliki, maka pengubahan data tiket akan gagal dan pengguna akan kembali ke menu admin.


**MENGHAPUS DATA TIKET**

<img width="340" height="343" alt="Screenshot 2026-10-06 214342" src="https://github.com/user-attachments/assets/043b3685-7500-4233-8cbb-31a289f1ab4e" />

Bagian ini ditemukan jika kita memilih pilihan 4, dimana kita dapat menghapus data tiket yang telah tersimpan, dan kita diberi pilihan untuk mengkonfirmasi apakah kita jadi menghapus data tiket atau tidak.

<img width="337" height="179" alt="Screenshot 2026-10-06 214630" src="https://github.com/user-attachments/assets/71df3aff-3511-46df-a03d-63097410ba87" />

Ini adalah suatu kondisi dimana kita membatalkan untuk menghapus data tiket.


**LOGOUT**

<img width="244" height="57" alt="Screenshot 2026-10-06 214753" src="https://github.com/user-attachments/assets/127f5a2b-17cc-4bd3-a5a6-dc3260acf10a" />

Bagian ini ditemukan jika kita memilih pilihan 5, layar akan otomatis dibersihkan karena didalam kode program terdapat kode os.system dan program dihentikan.


**MENU USER**

Dalam menu user, penggguna user hanya dapat memasukkan 2 pilihan antara melihat data dan logout.

<img width="285" height="318" alt="Screenshot 2026-10-06 215656" src="https://github.com/user-attachments/assets/5b92472c-0721-45e5-b679-17a7378e35af" />

Bagian ini ditemukan pada awal program setelah kita memasukkan username dan password dari user yang sesuai, maka tampilannya akan menampilkan ``menu user``.Jika salah, program akan menolak dan sama seperti kondisi di ``menu admin`` sebelumnya, program akan meminta login ulang.


**TAMPILKAN DATA TIKET**

<img width="279" height="338" alt="image" src="https://github.com/user-attachments/assets/c087bd19-798a-42a9-84ba-fce814184b1d" />

Bagian ini ditemukan ketika kita memilih pilihan 1, program akan menampilkan data yang tersedia.


**LOGOUT**

<img width="244" height="57" alt="Screenshot 2026-10-06 214753" src="https://github.com/user-attachments/assets/127f5a2b-17cc-4bd3-a5a6-dc3260acf10a" />

Bagian ini ditemukan jika kita memilih pilihan 5, layar akan otomatis dibersihkan karena didalam kode program terdapat kode os.system dan program dihentikan.


# PENJELASAN PENERAPAN NILAI TAMBAH

Program ini memiliki beberapa nilai tambah yang membuat program menjadi lebih menarik dan tidak terlalu sederhana. Nilai tambah tersebut berasal dari penggunaan beberapa library Python, yaitu ``os``, ``random``, dan ``pwinput``.

<img width="138" height="73" alt="Screenshot 2026-10-06 220649" src="https://github.com/user-attachments/assets/7ba839d4-339f-4cc5-a31c-a81f3aea9272" />


**IMPORT OS**

<img width="465" height="66" alt="Screenshot 2026-10-06 220656" src="https://github.com/user-attachments/assets/36d9dfea-b6c3-454c-a8af-c47609d572d7" />

Dalam kode program ini, library ``os`` digunakan untuk menjalankan fungsi membersihkan layar, jika ``os`` diaktifkan maka kita tidak perlu repot untuk mengetik ``cls`` secara manual karena akan otomatis dibersihkan oleh ``os.system``.


**IMPORT RANDOM**

<img width="364" height="163" alt="Screenshot 2026-10-06 221108" src="https://github.com/user-attachments/assets/d688b860-79a8-47fc-a44d-0eab574ba22d" />

Dalam kode program ini, library ``random``  digunakan untuk mengacak kode tiket sehingga kita tidak perlu input kode tiket lagi secara manual dan akan secara otomatis diacak oleh library random.


**IMPORT PWINPUT**

<img width="486" height="77" alt="Screenshot 2026-10-06 221330" src="https://github.com/user-attachments/assets/efe604c0-82ee-48c9-9496-120360f2c5c5" />

Dalam kode program ini, library ``pwinput`` digunakan agar password tidak terlihat ketika sedang diketik.


**ERROR HANDLING**

<img width="423" height="422" alt="Screenshot 2026-10-06 221559" src="https://github.com/user-attachments/assets/e35f347c-8969-4913-93d9-2abc1762e2a6" />

Pada bagian ini saya menggunakan error handling ``try-except`` untuk mencegah program berhenti atau mengalami error ketika pengguna memasukkan data yang tidak sesuai.













