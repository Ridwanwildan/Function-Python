# Latihan membuat function python  

* Nama          : Hizbullah Ridwan
* NIM           : 312110055
* Kelas         : TI.21.C.1
* Mata Kuliah   : Bahasa Pemrograman
----------------------------------
Dalam latihan membuat function [`python`](https://www.python.org/) ini, saya menggunakan [`PyCharm`](https://www.jetbrains.com/pycharm/) sebagai teks editornya.     
    
* [Latihan](https://github.com/Ridwanwildan/Dictionary-Python#latihan)         
* [Tugas](https://github.com/Ridwanwildan/Dictionary-Python#tugas)        

## Latihan      

Latihan mengubah function biasa menjadi `lambda function`. Ini merupaka function sebelum diubah ke lambda function :          
```bash
import math

def a(x):
    return x**2

def b(x, y):
    return math.sqrt(x**2 + y**2)

def c (*args):
    return sum(args)/len(args)

def d(s):
    return "".join(set(s))
```              
Ini yang sudah diubahnya :             
```bash
import math

a = lambda x: x**2

b = lambda x, y: math.sqrt(x**2 + y**2)

c = lambda *args: sum(args)/len(args)

d = lambda s: "".join(set(s))
```         

## Tugas           

Buat program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:             
* Fungsi `tambah()` untuk menambah data                
* Fungsi `tampilkan()` untuk menampilkan data                
* Fungsi `hapus(nama)` untuk menghapus data berdasarkan nama                
* Fungsi `ubah(nama)` untuk mengubah data berdasarkan nama                

![Gambar 1](screenshot/flowchart.PNG)         

Untuk menyimpan datanya kita akan menggunakan dictionary. Deklarasikan dictionary terlebih dulu :           
```bash
data = {
    "nim":[],
    "nama":[],
    "uts":[],
    "uas":[],
    "tugas":[]
}
```         

Setelah itu membuat fungsi `tambah()`. Jika user mengetik `T` atau `t` maka nantinya dia akan masuk kedalam menu tambah data. Didalam menu ini disediakan inputan untuk mengisi values dari dictionary yang masih kosong tadi. Kemudian kita pakai `append()`untuk memasukkan inputannya kedalam values.                             
```bash
def tambah():
     data["nim"].append(input("NIM         :"))
     data["nama"].append(input("Nama        :"))
     data["uts"].append(int(input("Nilai UTS   :")))
     data["uas"].append(int(input("Nilai UAS   :")))
     data["tugas"].append(int(input("Nilai Tugas :")))
```         
![Gambar 2](screenshot/img1.png)          

Selanjutnya buat fungsi `tampilkan()`. Selanjutnya ada menu lihat data. Untuk mengakses menu ini user bisa ketik `L` atau `l` dan nanti akan ada tampilan tabel yang berisi data data yang sudah ditambahkan tadi. Kita gunakan ***if len(data["nama"]) != 0*** yang artinya jika ada data maka tabel akan menampilkan keseluruhan data sebanyak n kali sesuai dengan ***len(data["nama"])*** dan jika tidak ada data sama sekali maka tabel akan menampilkan tulisan ***TIDAK ADA DATA***.          
```bash
def tampilkan():
     print("Daftar Nilai")
     print("==========================================================================")
     print("| No  |          Nama           |    NIM    | TUGAS | UTS | UAS |  AKHIR |")
     print("==========================================================================")
     if len(data["nama"]) != 0:
         for i in range(len(data["nama"])):
             print("|", i+1, "  |", end="")
             print('{0:<25}'.format(data["nama"][i]), end="")
             print("|", data["nim"][i], end="")
             print(" |", data["tugas"][i], end="")
             print("    |", data["uts"][i], end="")
             print("  |", data["uas"][i], " | ", end="")
             print(f'{(data["tugas"][i]*30/100) + (data["uts"][i]*35/100) + (data["uas"][i]*35/100) :.2f}', " |")
     else:
         print("                         TIDAK ADA DATA                               ")      
     print("==========================================================================")
```         
![Gambar 3](screenshot/img2.png)          
![Gambar 4](screenshot/img3.png)          

Fungsi menghapus data `hapus(nama)`. Untuk masuk ke menu ini ketik `H` atau `h`. User akan diminta untuk menginput nama yang akan dihapus datanya. Kemudian dicari nama tersebut ada di index ke berapa dengan `index()` dan nantinya index tersebut akan dihapus datanya.                 
```bash
def hapus():
    print("Hapus Data")
    hapus = input("Masukkan Nama yang akan dihapus : ")
    if hapus in data["nama"]:
        a = data["nama"].index(hapus)
        data["nim"].pop(a)
        data["nama"].pop(a)
        data["tugas"].pop(a)
        data["uts"].pop(a)
        data["uas"].pop(a)
    else:
        print("Nama", hapus, "tidak ada")
```         
![Gambar 4](screenshot/img4.png)          

Fungsi mengubah data `ubah(nama)`. Untuk masuk ke menu ini ketik `U` atau `u`. User akan diminta untuk menginput nama yang akan diubah datanya. Kemudian dicari nama tersebut ada di index ke berapa dengan `index()` dan nantinya index tersebut akan diubah datanya.                 
```bash
def ubah():
    print("Ubah Data")
    ubah = input("Masukkan Nama yang akan diubah : ")
    if ubah in data["nama"]:
        b = data["nama"].index(ubah)
        print("NIM sebelumnya : ", data["nim"][b])
        data["nim"][b] = input("Masukkan NIM yang baru : ")
        print("Nama sebelumnya : ", data["nama"][b])
        data["nama"][b] = input("Masukkan Nama yang baru : ")
        print("Nilai Tugas sebelumnya : ", data["tugas"][b])
        data["tugas"][b] = int(input("Masukkan Nilai Tugas yang baru : "))
        print("Nilai UTS sebelumnya : ", data["uts"][b])
        data["uts"][b] = int(input("Masukkan Nilai UTS yang baru : "))
        print("Nilai UAS sebelumnya : ", data["uas"][b])
        data["uas"][b] = int(input("Masukkan Nilai UAS yang baru : "))
        print("Data berhasil diubah")
    else:
        print("Nama", ubah, "tidak ada")
```         
![Gambar 4](screenshot/img5.png)          

Kemudian fungsi yang sudah dibuat atau dideklarasikan tadi, kita akan masukkan ke dalam while loop dan bisa dipanggil kapan saja.                
```bash
while True:
     menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]:")
     if menu == "t" or menu == "T":
         tambah()
     elif menu == "h" or menu == "H":
         hapus()
     elif menu == "u" or menu == "U":
         ubah()
     elif menu == "l" or menu == "L":
         tampilkan()     
     elif menu == "k" or menu == "K":
         break
     else:
         salah()
```         