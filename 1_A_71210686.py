#kalkulator sederhana

def calculator():
    print("="*8,"Calculator sederhana","="*8)
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")

calculator()

pilih=input("Masukkan pilihan: ")
b1=int(input("Masukkan bilangan 1: "))
b2=int(input("Masukkan bilangan 2: "))

def tambah():
    print("Hasilnya:",b1+b2)

def kurang():
    print("Hasilnya:",b1-b2)

def kali():
    print("Hasilnya:",b1*b2)

def bagi():
    print("Hasilnya:",b1/b2)

def pangkat():
    print("Hasilnya:",b1**b2)

if pilih=="1":
    tambah()
elif pilih=="2":
    kurang()
elif pilih=="3":
    kali()
elif pilih=="4":
    bagi()
elif pilih=="5":
    pangkat()
else:
    print("Hasilnya: Maaf input operasi antara 1-5")
