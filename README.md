# Setup Lengkap LEGO MINDSTORMS Robot Inventor (Set 51515)

---

## Daftar Isi

1. Persiapan  
2. Instal Aplikasi  
3. Sambungkan Hub  
4. Cek Konfigurasi Hardware / Motor  
5. Update OS / Firmware Hub & Komponen Tambahan  
6. Contoh Program Sederhana “Hello World”  
7. Penjelasan Istilah-Istilah Penting  
8. Letak Gambar di README  
9. Referensi Tambahan  

---

## 1. Persiapan

Sebelum mulai, pastikan:

- Semua bagian LEGO sudah ada: Hub, motor, sensor, kabel, baterai atau charger/power.  
- Komputer / tablet / HP kamu kompatibel dengan aplikasi LEGO Robot Inventor.  
- Ada koneksi internet agar bisa mengunduh aplikasi & melakukan update firmware.

---

## 2. Instal Aplikasi

- Jika kamu menggunakan **Windows**, buka Microsoft Store dan install lewat link ini:  
  `https://apps.microsoft.com/detail/9mtq0n7w1d6x?launch=true&mode=full&hl=en-us&gl=id&ocid=bingwebsearch`  
- Bila memakai **Mac / Android / iOS**, cari “LEGO MINDSTORMS Robot Inventor” di App Store / Google Play, lalu install seperti biasa.

---

## 3. Sambungkan Hub

- Nyalakan Hub LEGO kamu.  
- Sambungkan ke perangkat (komputer/tablet) lewat **Bluetooth** atau **USB**.  
- Kalau bingung caranya, lihat tutorial ini:  
  `https://www.youtube.com/watch?v=MEj1_pS3esw`

---

## 4. Cek Konfigurasi Hardware / Motor

Setelah Hub tersambung:

- Aplikasi akan meminta update OS Hub jika perlu.  
- Untuk melihat konfigurasi hardware/motor, klik tombol **“Open Hub connection”** di aplikasi (lihat Gambar 1).  
- Akan muncul tampilan seperti ini: status motor untuk tiap port (misalnya A, B, C, D, F, dst), dan nilai-nilai seperti **Power**, **Speed**, **Relative Position**, **Absolute Position**, dan lainnya (lihat Gambar 2).  

Berikut contoh tampilan konfigurasi motor:  
![Gambar 1: Open Hub connection](https://github.com/user-attachments/assets/ff60885e-ff1c-46f7-b478-a87426970cee)  
![Gambar 2: Konfigurasi motor & port](https://github.com/user-attachments/assets/1fe1ba9b-1212-4e0e-91ff-4dd6321325d4)

Penjelasan konfigurasi motor:

| Variabel              | Penjelasan                                                                 |
|------------------------|------------------------------------------------------------------------------|
| **Power**              | Seberapa besar tenaga (daya %) yang diberikan ke motor. Negatif = arah negatif / balik. |
| **Speed**              | Kecepatan motor sebagai persentase dari kecepatan maksimal.                |
| **Relative Position**  | Sudut motor relatif terhadap posisi saat Hub dinyalakan atau motor dipasang. |
| **Absolute Position**  | Posisi sudut absolut (biasanya dalam derajat), berdasarkan acuan tetap.     |
| **Port**               | Port tempat motor/sensor dipasang di Hub (contoh: A, B, C, D, F).          |

---

## 5. Update OS / Firmware Hub & Komponen Tambahan

- Pastikan Hub tersambung ke **charger** selama update agar tidak mati tiba-tiba.  
- Jika aplikasi mendeteksi ada update OS / firmware Hub, jalankan update tersebut.  
- Setelah selesai, aplikasi menjadi konfirmasi bahwa firmware dan konten sudah diperbarui.  
- Kalau ada motor atau sensor tambahan yang juga butuh update, lakukan sesuai instruksi aplikasi.

---

## 6. Contoh Program Sederhana “Hello World”

Gunakan kode berikut sebagai latihan pertama. Simpan file misalnya `hello_world.py`.

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
