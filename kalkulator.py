#program kalkulator menggunakan function x dan y 
#kita buat function
def jumlah(x,y):#ini untuk proses penjumlahan
    return x+y
def kurang (x,y):#ini untuk proses pengurangan
    return x-y
def kali (x,y):#ini untuk proses perkalian
    return x*y
def bagi (x,y): #ini untuk proses pembagian
    return x/y

print ("pilihan operasi hitung :")
print ("1.Penjumlahan")
print ("2.Pengurangan")
print ("3.Perkalian")
print ("4.Pembagian")

print ("ketikkan :1,2,3,4 pilih salah satu")
pilih=input("masukkan pilihan nomor")


angka_1=int(input("masukkan angka pertama: "))
angka_2=int(input("masukkan angka kedua: "))

if pilih=="1":
    print (angka_1,"+",angka_2,"=",jumlah(angka_1,angka_2))
elif pilih =="2":
    print (angka_1,"-",angka_2,"=",kurang(angka_1,angka_2))
elif pilih =="3":
    print (angka_1,"X",angka_2,"=",kali(angka_1,angka_2))
elif pilih =="4":
    print (angka_1,"/",angka_2,"=",bagi(angka_1,angka_2))

else:
    print("masukkan salah")
