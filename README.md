# Kasir Mini — RCA Software Testing

Aplikasi kasir desktop sederhana untuk demonstrasi tiga fault dan Root Cause Analysis (RCA). Tombol launcher membuka UI dengan implementasi fault agar hasilnya bisa direproduksi langsung.

## Menjalankan aplikasi demo fault
Klik dua kali **`aplikasi_fault/Jalankan_Aplikasi.bat`** (atau `Jalankan_Kasir.bat` di folder utama). Aplikasi ini sengaja mempertahankan tiga fault untuk direproduksi.

Untuk melihat F-01, isi nama `buku`, jumlah `2`, harga satuan `60000`, biarkan diskon kosong, dan isi pembayaran `120000`. Aplikasi fault menampilkan diskon **Rp1.200** karena memakai 1%, sedangkan aturan yang benar adalah 10% (Rp12.000). Untuk F-02, masukkan jumlah `0`; untuk F-03, masukkan jumlah `2`, harga `60000`, diskon manual `10`, dan pembayaran `120000`.

## Menjalankan aplikasi perbaikan
Klik dua kali **`aplikasi_perbaikan/Jalankan_Aplikasi.bat`**. Ini aplikasi terpisah dengan validasi, diskon 10%, dan kembalian yang benar. Kedua aplikasi memiliki folder dan source masing-masing.

## Tes
Dari terminal di folder project, jalankan satu perintah:

```powershell
python -m pytest -q
```

## Hasil RCA
Rincian tiga fault, test case, 5 Whys, dampak, fix, dan retest tersedia di [docs/RCA.md](docs/RCA.md). Catatan presentasi dan tanya jawab ada di [docs/PRESENTATION_NOTES_QA.md](docs/PRESENTATION_NOTES_QA.md). Slide deck `Kasir_Mini_RCA_EVIDENCE.pptx` memuat perbandingan screenshot aplikasi dan cuplikan kode salah/perbaikan untuk F-01, F-02, dan F-03.

## Isi folder
- `aplikasi_fault/` — aplikasi yang sengaja berisi fault untuk demonstrasi.
- `aplikasi_perbaikan/` — aplikasi terpisah dengan fault yang sudah diperbaiki.
- `Jalankan_Kasir.bat` — shortcut ke aplikasi demo fault.
- `src/` — antarmuka desktop dan logika kasir.
- `tests/` — tes normal, input batas, dan tiga fault.
- `screenshots/` — screenshot transaksi dan bukti reproduksi masing-masing fault.
- `docs/` — RCA dan bahan presentasi.
- `requirements.txt` — pytest untuk menjalankan tes.

Repository Git lokal sudah disiapkan. README ini juga dapat dijadikan petunjuk saat mengunggah folder tersebut ke GitHub.

Repository Git lokal sudah disiapkan. README ini juga dapat dijadikan petunjuk saat mengunggah folder tersebut ke GitHub.

