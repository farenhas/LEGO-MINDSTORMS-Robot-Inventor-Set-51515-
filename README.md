# Setup Lengkap LEGO MINDSTORMS Robot Inventor (Set 51515)

---

## Daftar Isi

1. Persiapan  
2. Instal Aplikasi  
3. Sambungkan Hub  
4. Cek Konfigurasi Hardware / Motor  
5. Update OS / Firmware Hub & Komponen Tambahan  
6. Contoh Program Sederhana “Hello World”  
7. Penjelasan Istilah-istilah Penting  
8. Letak Gambar di README  
9. Referensi Tambahan  

---

## 1. Persiapan

Sebelum mulai:

- Pastikan paket LEGO lengkap: Hub, motor, sensor, kabel, baterai atau charger/power.  
- Siapkan komputer / tablet / HP yang kompatibel dengan aplikasi LEGO Robot Inventor.  
- Siapkan koneksi internet agar bisa download aplikasi & update firmware.  

---

## 2. Instal Aplikasi

- Jika kamu memakai **Windows**, buka Microsoft Store dan install dengan link ini:  
  `https://apps.microsoft.com/detail/9mtq0n7w1d6x?launch=true&mode=full&hl=en-us&gl=id&ocid=bingwebsearch`  
- Jika memakai **Mac / Android / iOS**, cari “LEGO MINDSTORMS Robot Inventor” di App Store / Google Play, lalu instal seperti biasa.

---

## 3. Sambungkan Hub

- Nyalakan Hub LEGO kamu.  
- Hubungkan ke perangkat (komputer/tablet) lewat **Bluetooth** atau **USB**.
- Atau bisa lihat tutorial lebih lengkap ke link : https://www.youtube.com/watch?v=MEj1_pS3esw

---

## 4. Cek Konfigurasi Hardware / Motor

Setelah hub tersambung:

Nantinya akan update Hub OS
 ![WhatsApp Image 2025-09-22 at 18 36 58_2bcd7229](https://github.com/user-attachments/assets/3453efde-8a11-4c43-a5e4-65e4674ac9f4)
 ![WhatsApp Image 2025-09-22 at 18 42 12_3e8fa03c](https://github.com/user-attachments/assets/e9a868be-ef54-490e-bdc2-c845ff84f9f2)

- Untuk melihat konfigurasi, Klik tombol **“Open Hub connection”** di aplikasi
  ![WhatsApp Image 2025-09-22 at 19 11 11_b40d98f7](https://github.com/user-attachments/assets/ff60885e-ff1c-46f7-b478-a87426970cee)

- Aplikasi akan menunjukkan status motor / port (A, B, C, D, F, dll), serta nilai-nilai seperti power, speed, relative position, position absolut, dsb.  
![WhatsApp Image 2025-09-22 at 19 11 20_0a645ad9](https://github.com/user-attachments/assets/1fe1ba9b-1212-4e0e-91ff-4dd6321325d4)
  contoh tampilan konfigurasi, seperti port motor & nilai-nilai tersebut.

Penjelasan konfigurasi motor:

| Variabel            | Penjelasan                                                                |
|----------------------|------------------------------------------------------------------------|
| **Power**            | Seberapa besar tenaga (daya %) yang diberikan ke motor. Negatif = arah balik. |
| **Speed**            | Kecepatan putaran motor dalam persentase terhadap kecepatan maksimum.  |
| **Relative Position**| Posisi sudut relatif terhadap posisi saat hub dinyalakan atau motor dipasang. |
| **Absolute Position**| Posisi sudut absolut (biasanya dalam derajat) berdasarkan acuan tetap. |
| **Port**             | Tempat pemasangan motor/sensor di Hub, misalnya A, B, C, D, F.         |

---

## 5. Update OS / Firmware Hub & Komponen Tambahan

- Pastikan Hub terhubung ke **charger** selama proses update agar tidak mati tiba-tiba.  
- Jika aplikasi mendeteksi ada update OS / firmware Hub, jalankan update tersebut.  
- Setelah update selesai, aplikasi akan muncul konfirmasi bahwa firmware + konten sudah diperbarui.  
- Bila ada motor atau sensor tambahan yang juga perlu update, lakukan juga sesuai instruksi aplikasi.

---

## 6. Contoh Program Sederhana “Hello World”

Kode berikut bisa kamu pakai sebagai latihan pertama. Simpan dengan nama misalnya `hello_world.py`.

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

kemudian untuk menjalankan klik tombol run di sisi kanan bawah 
![WhatsApp Image 2025-09-22 at 19 18 56_efdc8782](https://github.com/user-attachments/assets/b881df23-c050-4129-aadb-ceee4dc6f180)

