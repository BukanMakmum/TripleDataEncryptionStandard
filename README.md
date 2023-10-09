# Triple Data Encryption Standard

Implementasi sederhana algoritma Triple Data Encryption Standard (3DES) menggunakan Python dan pustaka Tkinter untuk antarmuka pengguna grafis. Triple Data Encryption Standard (3DES) versi Education merupakan skrip yang dikembangkan untuk pembelajaran proses enkripsi dan dekripsi menggunakan 3DES.

## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Tangkapan Layar](#tangkapan-layar)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

## Pendahuluan

Triple Data Encryption  Standard (3DES)  merupakan  salah satu algoritma simetris pada kriptografi yang digunakan untuk mengamankan  data dengan cara menyandikan data. Proses yang dilakukan dalam penyandian  datanya, yaitu proses enkripsi dan proses dekripsi. Algoritma 3DES adalah suatu algoritma pengembangan  dari algoritma DES (Data Encryption Standard). Perbedaan DES dengan 3DES terletak pada panjangnya  kunci yang digunakan. Pada DES menggunakan  satu kunci yang panjangnya 56-bit, sedangkan pada 3DES menggunakan 3 kunci yang panjangnya 168- bit (masing-masing  panjangnya  56-bit). Pada 3DES, 3 kunci yang digunakan  bisa bersifat saling bebas (K1  ≠ K2  ≠ K3) atau hanya dua buah kunci yang saling bebas dan satu kunci lainnya sama dengan kunci pertama (K1 ≠ K2 dan K3 = K1). Karena tingkat kerahasiaan algoritma 3DES terletak pada panjangnya  kunci yang digunakan,  maka penggunaan  algoritma 3DES dianggap lebih aman dibandingkan dengan algoritma DES.


## Fitur

- Enkripsi dan Dekripsi menggunakan 3DES;
- Input berupa 16 digit Heksadesimal;
- Output berupa 16 digit Heksadesimal dan 64 bit dalam biner;
- Validasi input key dan teks plaintext/ciphertext;
- Menampilkan dan simpan hasil Debug Result Enkripsi dan Dekripsi (Khusus v2.0.beta setelahnya)
- Reset input; dan
- Tampilan modern menggunakan tkinter/antarmuka grafis yang ramah pengguna.
  
- Contoh Input dan Output
  ```bash
  Plaintext:   0123456789ABCDEF
  Key 1:       3E87044D8F1C2D7F
  Key 2:       1A1A2DDB7494C5AA
  Key 3:       AABB09182736CCDD
  Ciphertext:  C191030A5A4E9FDB
   ```

## Instalasi

1. Clone repositori ini:

   ```bash
   git clone https://github.com/BukanMakmum/TripleDataEncryptionStandard.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd TripleDataEncryptionStandard
   ```

3. Instal pustaka yang diperlukan:

   ```bash
   pip install tk
   pip install ttkthemes

   ```

## Penggunaan

1. Jalankan aplikasinya:

   ```bash
   3DESvx.x.py atau 3DESvx.x.exe
   x.x = nomor versi
   ```

2. Masukkan 16 digit heksadesimal (64 bit) Plaintext/Ciphertext dan Key 1, 2 dan 3.

3. Klik tombol "Enkripsi" atau "Dekripsi" sesuai kebutuhan.

4. Hasil akan ditampilkan di bidang "Hasil".

## Tangkapan Layar

![hasil](https://github.com/BukanMakmum/TripleDataEncryptionStandard/assets/32379649/04f0e6d6-b18f-4b45-8643-dd2f88a816c4)

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
