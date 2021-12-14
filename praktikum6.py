data = {
    "nim":[],
    "nama":[],
    "uts":[],
    "uas":[],
    "tugas":[]
}

#deklarasi fungsi
#tambah
def tambah():
     data["nim"].append(input("NIM         :"))
     data["nama"].append(input("Nama        :"))
     data["uts"].append(int(input("Nilai UTS   :")))
     data["uas"].append(int(input("Nilai UAS   :")))
     data["tugas"].append(int(input("Nilai Tugas :")))

#tampilkan
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

#hapus
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

#ubah
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

#salah ketik
def salah():
    print("Maaf, perintah yang diketik salah")

#Running program
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

