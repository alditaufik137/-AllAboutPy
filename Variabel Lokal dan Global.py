Nama = "Mochamad Aldi Taufik"
Umur = "19 Tahun"
Pekerjaan = "Mahasiswa"
Status_Pernikahan = "Belum Menikah"
Agama = "Islam"

def lokal():
          #lokal
          jurusan = "Teknik Informatika"
          fakultas= "Teknologi Industri"
          #akses variable lokal
          print ("jurusan : %s"% jurusan)
          print ("fakultas: %s"% fakultas)
#global
print ("Nama: %s"%Nama)
print ("Umur: %s"%Umur)
print ("Pekerjaan: %s"%Pekerjaan)
print ("Status_Pernikahan : %s"%Status_Pernikahan)
print ("Agama: %s"%Agama)
#panggil lokal
lokal()
