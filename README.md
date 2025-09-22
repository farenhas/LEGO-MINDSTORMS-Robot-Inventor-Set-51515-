# Setup Lengkap LEGO MINDSTORMS Robot Inventor (Set 51515)

---

## Daftar Isi

1. Persiapan
2. Instal Aplikasi
3. Sambungkan Hub
4. Cek Konfigurasi Hardware / Motor
5. Update OS / Firmware Hub & Komponen Tambahan
6. Contoh Program Sederhana "Hello World"
7. Penjelasan Istilah-Istilah Penting
8. Referensi Tambahan

---

## 1. Persiapan

Sebelum mulai, pastikan:

- Semua bagian LEGO sudah ada: Hub, motor, sensor, kabel, baterai atau charger/power.
- Komputer / tablet / HP kamu kompatibel dengan aplikasi LEGO Robot Inventor.
- Ada koneksi internet agar bisa mengunduh aplikasi & melakukan update firmware.

---

## 2. Instal Aplikasi

- **Windows**: Unduh di Microsoft Store lewat link berikut:
  [LEGO Robot Inventor App](https://apps.microsoft.com/detail/9mtq0n7w1d6x?launch=true&mode=full&hl=en-us&gl=id&ocid=bingwebsearch)
- **Mac / Android / iOS**: Cari "LEGO MINDSTORMS Robot Inventor" di App Store / Google Play, lalu install seperti biasa.

---

## 3. Sambungkan Hub

- Nyalakan Hub LEGO kamu.
- Sambungkan ke perangkat (komputer/tablet) lewat **Bluetooth** atau **USB**.
- Jika masih bingung, ikuti tutorial:
  [Cara menghubungkan Hub LEGO](https://www.youtube.com/watch?v=MEj1_pS3esw)

---

## 4. Cek Konfigurasi Hardware / Motor

Setelah Hub tersambung:

- Aplikasi akan meminta update OS Hub jika perlu.
- Untuk melihat konfigurasi hardware/motor, klik **"Open Hub connection"** di aplikasi.

Contoh tampilan:

<p align="center">
  <img src="https://github.com/user-attachments/assets/ff60885e-ff1c-46f7-b478-a87426970cee" alt="Gambar 1: Open Hub connection" width="400"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/1fe1ba9b-1212-4e0e-91ff-4dd6321325d4" alt="Gambar 2: Konfigurasi motor & port" width="400"/>
</p>

Penjelasan konfigurasi motor:

| Variabel              | Penjelasan                                                                 |
|------------------------|------------------------------------------------------------------------------|
| **Power**              | Besar tenaga (%) yang diberikan ke motor. Negatif = arah berlawanan.        |
| **Speed**              | Kecepatan motor sebagai persentase dari kecepatan maksimum.                |
| **Relative Position**  | Sudut motor relatif terhadap saat Hub dinyalakan / motor dipasang.          |
| **Absolute Position**  | Posisi sudut absolut (dalam derajat), dengan acuan tetap.                   |
| **Port**               | Port tempat motor/sensor dipasang di Hub (contoh: A, B, C, D, F).           |

---

## 5. Update OS / Firmware Hub & Komponen Tambahan

- Pastikan Hub tersambung ke **charger** selama update.
- Jika ada update OS / firmware, jalankan sampai selesai.
- Lakukan juga update untuk motor atau sensor tambahan bila diminta oleh aplikasi.

Contoh ketika aplikasi meminta update motor:

![WhatsApp Image 2025-09-22 at 18 42 54_1e67001f](https://github.com/user-attachments/assets/0057d1b7-1d91-49dc-b49b-c124edc11719)

---

## 6. Contoh Program Sederhana "Hello World"

Buat file `hello_world.py` dengan isi berikut:

```python
import hub
import runtime
import sys
import system

async def run(vm, stack):
    vm.broadcast("run")

async def display(vm, stack):
    await vm.system.display.write_async("Hello world")

async def sound(vm, stack):
    await vm.system.sound.play_async("/extra_files/Hello")
    await vm.system.sound.play_async("/extra_files/Celebrate")

async def cancel(vm, stack):
    vm.stop_stacks(except_stack=stack)
    hub.display.clear()
    hub.sound.beep(0, 0)

def setup(rpc, system, stop):
    vm = runtime.VirtualMachine(rpc, system, stop, "hello_world")
    vm.register_on_start("run_on_start", run)
    vm.register_on_broadcast("display_on_run", display, "run")
    vm.register_on_broadcast("sound_on_run", sound, "run")
    vm.register_on_button("cancel_on_left_button", cancel, "left", "pressed")
    vm.register_on_button("run_on_right_button", run, "right", "pressed")
    return vm

setup(None, system.system, sys.exit).start()
```

Untuk menjalankan program, klik tombol Run pada aplikasi:

<p align="center">
  <img src="https://github.com/user-attachments/assets/36721c45-9a89-444c-a69a-a2900cc316b0" alt="Tombol Run di aplikasi" width="400"/>
</p>

Penjelasan Singkat Kode:

- **display**: Menampilkan teks "Hello world" di layar Hub.
- **sound**: Memainkan suara "Hello" lalu "Celebrate".
- **cancel**: Menghentikan program dan membersihkan layar/suara.
- **setup**: Mengatur event seperti tombol ditekan atau broadcast sinyal agar program bisa berjalan otomatis.

---

## 7. Penjelasan Istilah-Istilah Penting

- **Hub**: Otak utama LEGO Inventor, mirip komputer mini.
- **Port**: Lubang koneksi di Hub untuk motor atau sensor.
- **Firmware**: Sistem operasi kecil yang ada di Hub.
- **Runtime**: Lingkungan eksekusi agar program bisa berjalan.
- **Broadcast**: Cara untuk mengirim sinyal antar bagian kode.

---

## 8. Referensi Tambahan

- [Dokumentasi Resmi LEGO MINDSTORMS](https://lego.github.io)
- [Channel YouTube LEGO Education](https://youtube.com/legoeducation)

Untuk belajar lebih dalam:

- **Dokumentasi resmi Motor API Robot Inventor**: menjelaskan mode power, speed, posisi relatif & absolut.
  [lego.github.io](https://lego.github.io)
- **Quick Reference fungsi hub, motor & sensor dari Pybricks** untuk set 51515.
  [pybricks.com](https://pybricks.com)
